#19101185 강동현 - All Pairs Shortest

import sys

n = int(sys.stdin.readline())
cost = []
for _ in range(n):
    s = list(map(int , sys.stdin.readline().split(" ")))
    cost.append(s)

for k in range(0,n):
    cost[k][k] = 0
    for i in range(0,n):
        for j in range(0,n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(0,n):
    for t in range(0,n):
        print(cost[i][t], end=" ")
    print("")