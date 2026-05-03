from evaluation.datasets.loader import load_dataset
from evaluation.metrics.basic_metrics import exact_match, f1_score
from evaluation.metrics.retrieval_metrics import context_recall, context_precision
from evaluation.metrics.hallucination import hallucination_check
from app.services.rag_service import run_rag
from langsmith import Client
from langsmith import traceable

from evaluation.metrics.generation_metrics import (
    answer_length,
    contains_key_phrase,
    brevity_penalty
)
from evaluation.metrics.reasoning import (
    reasoning_coverage,
    reasoning_completeness
)

@traceable(name="rag_evaluation_run")
def traced_run(model, question):
    return run_rag(model, question)

client = Client()


def evaluate(models, dataset_path):
    dataset = load_dataset(dataset_path)

    results = []

    for sample in dataset:
        question = sample["question"]
        truth = sample["ground_truth_answer"]

        for model in models:
            # traced automatically via @trace
            output = traced_run(model, question)

            retrieved_chunks = output["context"].split("\n")
            answer = output["answer"]

            result = {
                "model": model,
                "question": question,

                # core metrics
                "exact_match": exact_match(answer, truth),
                "f1": f1_score(answer, truth),

                # retrieval
                "context_recall": context_recall(
                    retrieved_chunks,
                    sample["expected_evidence_chunks"]
                ),
                "context_precision": context_precision(
                    retrieved_chunks,
                    sample["expected_evidence_chunks"]
                ),

                # hallucination
                "hallucination": hallucination_check(
                    answer,
                    sample["negative_sample"]
                ),

                # generation
                "answer_length": answer_length(answer),
                "semantic_overlap": contains_key_phrase(answer, truth),
                "brevity_penalty": brevity_penalty(answer, truth),

                # reasoning
                "reasoning_coverage": reasoning_coverage(
                    answer,
                    sample["reasoning_chain"]
                ),
                "reasoning_completeness": reasoning_completeness(
                    answer,
                    sample["reasoning_chain"]
                ),

                "difficulty": sample["difficulty"]
            }

            results.append(result)

            # 🔗 LangSmith feedback (auto-linked to current trace)
            try:
                client.create_feedback(
                    run_id=None,
                    key="f1",
                    score=result["f1"]
                )

                client.create_feedback(
                    run_id=None,
                    key="hallucination",
                    score=1 - result["hallucination"]
                )

                client.create_feedback(
                    run_id=None,
                    key="context_recall",
                    score=result["context_recall"]
                )

                client.create_feedback(
                    run_id=None,
                    key="reasoning_coverage",
                    score=result["reasoning_coverage"]
                )

            except Exception as e:
                print(f"LangSmith logging failed: {e}")

    return results