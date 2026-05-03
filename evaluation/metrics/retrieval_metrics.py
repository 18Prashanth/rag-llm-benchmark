def context_recall(retrieved, expected):
    hits = sum(1 for e in expected if any(e in r for r in retrieved))
    return hits / len(expected) if expected else 0


def context_precision(retrieved, expected):
    hits = sum(1 for r in retrieved if any(e in r for e in expected))
    return hits / len(retrieved) if retrieved else 0