def reasoning_coverage(answer, reasoning_steps):
    """
    Checks how many reasoning steps are reflected in the answer.
    """
    answer_lower = answer.lower()

    hits = 0
    for step in reasoning_steps:
        keywords = step.lower().split()

        if any(k in answer_lower for k in keywords):
            hits += 1

    return hits / len(reasoning_steps) if reasoning_steps else 0


def reasoning_completeness(answer, reasoning_steps):
    """
    Strict version: all steps must be represented.
    """
    answer_lower = answer.lower()

    for step in reasoning_steps:
        if not any(word in answer_lower for word in step.lower().split()):
            return 0

    return 1