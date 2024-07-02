def linear_search(li: list, target):
    """
    Returns index of the element's position in the list
    """

    # len(li) is a constant time operation meaning calculating it everytime is constant as it is said by py docs (len is cached so it wouldn't matter how many times we call it)
    # subscripting (i.e, li[1] or li[33]) is also a constant time operation as said by the docs
    for i in range(0, len(li)):
        if li[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Found at index:", index)
    else:
        print("Not found in the list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 1)

if __name__ == "__main__":
    verify(result)

"""
Why this program is an algorithm?
- returns a result in each case
- executes in a finite time
- returns expected result
"""
