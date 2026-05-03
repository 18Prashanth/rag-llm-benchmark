def hallucination_check(answer, negative_sample):
    return int(negative_sample.lower() in answer.lower())