#19101185 강동현 - 19101185 강동현 알고리즘 DPCoinChange

import sys
coin = list(map(int ,sys.stdin.readline().split(", ")))
money = int(sys.stdin.readline())
c = [10001 for i in range(0,money+1)]
c[0] = 0
k = len(coin)
for j in range(1,money+1,1):
    for i in range(0,k,1):
        if coin[i] <= j and c[j-coin[i]] + 1 < c[j]:
            c[j] = c[j-coin[i]] + 1
print(c[money])


