import timeit
import random
from merge_sort import merge_sort
from insertion_sort import insertion_sort

data = [random.randint(0, 10000) for _ in range(600)]

def tim_sort(arr):
    return sorted(arr)


merge_sort_time = timeit.timeit('merge_sort(data)', globals=globals(), number=10)
insertion_sort_time = timeit.timeit('insertion_sort(data)', globals=globals(), number=10)
tim_sort_time = timeit.timeit('tim_sort(data)', globals=globals(), number=10)

print(f"Merge Sort Time: {merge_sort_time:.7f} seconds")
print(f"Insertion Sort Time: {insertion_sort_time:.7f} seconds")
print(f"Timsort Time: {tim_sort_time:.7f} seconds")