#19101185 강동현 - Minimum Spanning Tree (MST)

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

def Find(x):
    if union_stack[x] == x:
        return x
    else:
        y = Find(union_stack[x])
        union_stack[x] = y
        return y

def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x != y:
        union_stack[y] = x


n, m = map(int, sys.stdin.readline().split())
graph = []
union_stack = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append([c, a, b])

graph = array_quicksort(graph)

count = 0
ans = 0
for i in range(m):

    dis = graph[i][0]
    start = graph[i][1]
    end = graph[i][2]

    if Find(start) != Find(end):
        Union(start, end)
        ans += dis
        count += 1

    if count == n - 1:
        break

print(ans)