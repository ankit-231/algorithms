def recursive_binary_search(li, target):
    if len(li) == 0:
        return False

    else:
        first_index = 0
        last_index = len(li) - 1
        midpoint = (first_index + last_index) // 2
        if li[midpoint] == target:
            return True
        elif li[midpoint] < target:
            return recursive_binary_search(li[: midpoint - 1], target)
        else:
            return recursive_binary_search(li[midpoint + 1 :], target)


from linear_search import numbers

result = recursive_binary_search(numbers, 100)

print(result)
