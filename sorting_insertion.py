#!/usr/bin/env python3

from typing import List

def insertion_sort(data: List[int]) -> None:
    for i in range(1, len(data)):
        j = i - 1
        while j >= 0 and data[j + 1] < data[j]:
            data[j], data[j + 1] = data[j + 1], data[j]
            j -= 1
        print(data)

if __name__=="__main__":
    data = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    insertion_sort(data)
