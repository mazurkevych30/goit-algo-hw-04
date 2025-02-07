def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
	# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def merge_k_lists(arr):
    temp = []
    i = 0

    while i < len(arr):
        temp = merge(temp, arr[i])
        i += 1

    return temp

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
MERGED_LIST = merge_k_lists(lists)
print("Відсортований список:", MERGED_LIST)
