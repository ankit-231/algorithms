def merge_sort(array):
    
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # If there are any remaining elements in left or right, add them
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array


# Example usage
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(array)
    print("Sorted array:", sorted_array)
