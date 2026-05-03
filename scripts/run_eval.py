from evaluation.runners.batch_eval import evaluate
from evaluation.runners.report import summarize


if __name__ == "__main__":
    models = ["gpt", "gemini"]

    results = evaluate(models, "evaluation/datasets/traffic_rules.json")

    summarize(results)