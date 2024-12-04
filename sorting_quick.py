#!/usr/bin/env python3

from typing import List

def sorting_quick(data: List[int]) -> None:
    sorting_quick_helper(data, 0, len(data) - 1)

def sorting_quick_helper(data: List[int], start: int, end: int) -> None:
    if end - start + 1 <= 1:
        return

    pivot = data[end]
    left = start

    for i in range(start, end):
        if data[i] < pivot:
            data[i], data[left] = data[left], data[i]
            left += 1

    data[end] = data[left]
    data[left] = pivot

    sorting_quick_helper(data, start, left - 1)
    sorting_quick_helper(data, left + 1, end)

if __name__=="__main__":
    data = [9, 8, 7, 4, 3, 2, 1, 6, 5]

    sorting_quick(data)
    print(data)
