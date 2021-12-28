#19101185 강동현 - Set Cover

import sys

n = int(sys.stdin.readline())
u = []
s = []
for i in range(1,n+1):
    u.append(i)
    sub = list(map(int , sys.stdin.readline().split(" ")))
    s.append(sub)
u = set(u)
ans = []
check = [1] * (n+1)

while u:
    idx = 0
    maxx = 0
    for i in range(0,len(s)):
        len_set = (len(u & set(s[i])))
        if len_set > maxx and check[i] == 1:
            maxx = len_set
            idx = i
    u = u - set(s[idx])
    check[idx] = 0
    ans.append(idx+1)
ans.sort()
for i in range(0,len(ans)-1):
    print(ans[i],end=" ")
print(ans[len(ans)-1])