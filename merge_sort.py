from typing import List, Tuple

random_numbers = [5, 10, 8, 7, 3, 9, 6, 1, 4, 2]


def merge_sort(li: List):
    if len(li) <= 1:
        return li

    left_half, right_half = split(li)

    print("l-r-h", left_half, right_half)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    print("--", left, right)
    merged_ = merge(left, right)
    print("m-", merged_)
    return merged_


def merge(left: List, right: List) -> List:
    l = []
    i = 0
    j = 0

    # - individual lists are compared and sorted: [5] and [8]
    # - multiple lists are compared: [5, 3] and [8, 1] and so on ...

    # hint: print the value of i and j to see how they increment which if or else condition is True
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # note that i is not reset but has the value of above i from the above loop
    # same for j
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l


def split(li: List) -> Tuple[List, List]:
    midpoint = len(li) // 2
    left_half = li[:midpoint]
    right_half = li[midpoint:]
    return left_half, right_half


if __name__ == "__main__":
    # numbers.pop()
    merged = merge_sort(random_numbers)
    print(merged)
