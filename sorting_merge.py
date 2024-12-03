#!/usr/bin/env python3

from typing import List

def sorting_merge(data: List[int]) -> None:
    return sorting_merge_helper(data, 0, len(data) - 1)

def sorting_merge_helper(data: List[int], start: int, end: int) -> List[int]:
    if end - start + 1 <= 1:
        return data

    middle = start + (end - start) // 2

    sorting_merge_helper(data, start, middle)
    sorting_merge_helper(data, middle + 1, end)

    sorting_merger(data, start, middle, end)

    return data

def sorting_merger(data: List[int], start: int, middle: int, end: int) -> None:
    left = data[start: middle + 1]
    right = data[middle + 1: end + 1]

    i = 0
    j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

    print(data)

if __name__=="__main__":
    data = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    sorting_merge(data)
