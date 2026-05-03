from collections import defaultdict


def summarize(results):
    summary = defaultdict(lambda: defaultdict(list))

    for r in results:
        model = r["model"]
        for key in ["exact_match", "f1", "context_recall", "context_precision", "hallucination"]:
            summary[model][key].append(r[key])

    for model in summary:
        print(f"\n=== {model.upper()} ===")
        for metric in summary[model]:
            values = summary[model][metric]
            avg = sum(values) / len(values)
            print(f"{metric}: {avg:.3f}")