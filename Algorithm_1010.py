#19101185 강동현 - Knapsack

import sys

n , w = map(int , sys.stdin.readline().split(" "))
stack = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split(" "))
    stack.append([b,a])
dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
for i in range(0,len(stack)):
    for t in range(0,w+1):
        if t < stack[i][0]:
            dp[i][t] = dp[i-1][t]
        else:
            dp[i][t] = max((stack[i][1] + dp[i-1][t-stack[i][0]]) , (dp[i-1][t]))
print(max(dp[n-1]))