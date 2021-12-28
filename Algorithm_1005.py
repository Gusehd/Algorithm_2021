#19101185 강동현 - 1K sorting

import sys

def array_quicksort(list):
    if len(list) <= 1 : return list
    pivot = list[len(list) // 2]
    less_arr , equal_arr , big_arr = [] , [] , []
    for i in list:
        if i < pivot : less_arr.append(i)
        elif i > pivot : big_arr.append(i)
        else: equal_arr.append(i)
    return array_quicksort(less_arr) + equal_arr + array_quicksort(big_arr)

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    stack.append(int(sys.stdin.readline()))
stack = array_quicksort(stack)
for i in range(0,n):
    print(stack[i])