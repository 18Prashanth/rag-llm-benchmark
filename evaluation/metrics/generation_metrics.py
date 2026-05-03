import re


def normalize(text):
    return re.sub(r"\s+", " ", text.lower().strip())


def answer_length(answer):
    return len(answer.split())


def contains_key_phrase(answer, ground_truth):
    """
    Checks if key phrases from ground truth appear in answer.
    """
    truth_tokens = set(normalize(ground_truth).split())
    answer_tokens = set(normalize(answer).split())

    overlap = truth_tokens & answer_tokens
    return len(overlap) / len(truth_tokens) if truth_tokens else 0


def brevity_penalty(answer, ground_truth):
    """
    Penalize overly long or overly short answers.
    """
    len_ratio = len(answer.split()) / max(len(ground_truth.split()), 1)

    if len_ratio < 0.5:
        return 0.5  # too short
    elif len_ratio > 2:
        return 0.5  # too long
    return 1.0