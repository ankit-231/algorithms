from linear_search import numbers, verify


def binary_search(li: list, target):
    first = 0
    last = len(li) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if li[midpoint] == target:
            return midpoint
        elif li[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


result = binary_search(numbers, 7)

verify(result)
