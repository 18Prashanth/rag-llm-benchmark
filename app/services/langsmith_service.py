from langsmith import traceable


def trace(func):
    return traceable(name=func.__name__)(func)