import re


def normalize(text):
    return re.sub(r"\s+", " ", text.lower().strip())


def exact_match(pred, truth):
    return int(normalize(pred) == normalize(truth))


def f1_score(pred, truth):
    pred_tokens = normalize(pred).split()
    truth_tokens = normalize(truth).split()

    common = set(pred_tokens) & set(truth_tokens)

    if len(common) == 0:
        return 0

    precision = len(common) / len(pred_tokens)
    recall = len(common) / len(truth_tokens)

    return 2 * (precision * recall) / (precision + recall)