from typing import List, Tuple
from linear_search import numbers


def merge_sort(li: List):
    if len(li) <= 1:
        return li

    left_half, right_half = split(li)

    print(left_half, right_half)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def merge(left: List, right: List) -> List:
    pass


def split(li: List) -> Tuple[List, List]:
    midpoint = len(li) // 2
    left_half = li[:midpoint]
    right_half = li[midpoint:]
    return left_half, right_half


# if __name__ == "__main__":
#     merge_sort(numbers)
