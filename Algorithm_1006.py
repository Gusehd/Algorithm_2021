#19101185 강동현 - Closest Pair (easy)

import sys
#x,y는 정수 , 입력값 1000개 , 하드 만개
n = int(sys.stdin.readline())
pl = [list(map(int, input().split(", "))) for i in range(n)]

def array_quicksort(list):
    if len(list) <= 1 : return list
    pivot = list[len(list) // 2]
    less_arr , equal_arr , big_arr = [] , [] , []
    for i in list:
        if i < pivot : less_arr.append(i)
        elif i > pivot : big_arr.append(i)
        else: equal_arr.append(i)
    return array_quicksort(less_arr) + equal_arr + array_quicksort(big_arr)

def array_quicksort_y(arr, nx = 1):
    if len(arr) <= 1: return arr
    i = len(arr) // 2
    pivot = arr[i]
    less = []; equal = []; greater = []
    for x in arr:
        if x[nx] < pivot[nx]:     less.append(x)
        elif x[nx] == pivot[nx]:  equal.append(x)
        elif x[nx] > pivot[nx]:   greater.append(x)
    return array_quicksort_y(less, nx) + equal + array_quicksort_y(greater, nx)

pl = array_quicksort(pl)

def getline(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def closet(start, end):
    if start == end:
        return float('inf')
    if end - start == 1:
        return getline(pl[start], pl[end])

    mid = (start + end) // 2
    min_stack = min(closet(start, mid), closet(mid, end))

    target_pl = []
    for i in range(start, end + 1):
        if (pl[mid][0] - pl[i][0]) ** 2 < min_stack:
            target_pl.append(pl[i])
    target_pl = array_quicksort_y(target_pl)

    t = len(target_pl)

    for i in range(t - 1):
        for j in range(i + 1, t):
            if (target_pl[i][1] - target_pl[j][1]) ** 2 < min_stack:
                min_stack = min(min_stack, getline(target_pl[i], target_pl[j]))
            else:
                break
    return min_stack

ans = closet(0, n - 1)
ans = round(ans ** 0.5,6)
print(ans)