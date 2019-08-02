from typing import List


def latest(scores: List[int]) -> int:
    return scores.pop()


def personal_best(scores: List[int]) -> int:
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores: List[int]) -> List[int]:
    scores.sort(reverse=True)
    return scores[:3]
