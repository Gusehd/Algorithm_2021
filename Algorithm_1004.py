#19101185 강동현 - Hunting the Monster

import sys

def array_quicksort(arr, nx = 0, desc = False):
    if len(arr) <= 1: return arr
    i = len(arr) // 2
    pivot = arr[i]
    less = []; equal = []; greater = []
    for x in arr:
        if x[nx] < pivot[nx]:     less.append(x)
        elif x[nx] == pivot[nx]:  equal.append(x)
        elif x[nx] > pivot[nx]:   greater.append(x)
    if desc:
        return array_quicksort(greater, nx, True) + equal + array_quicksort(less, nx, True)
    else:
        return array_quicksort(less, nx, False) + equal + array_quicksort(greater, nx, False)


hp = int(sys.stdin.readline())
n = int(sys.stdin.readline())
stack = []
ans = 0
for _ in range(n):
    a , b = map(int, sys.stdin.readline().split())
    stack.append([a,b,(a*b)])
stack = array_quicksort(stack,0,True)

for i in range(0,len(stack)):
    if hp < 1:
        break
    if hp >= stack[i][2]:
        hp -= stack[i][2]
        ans += stack[i][1]
    else:
        aa = hp // stack[i][0]
        if hp % stack[i][0] == 0:
            hp = 0
            ans += aa
        else:
            hp = 0
            ans += (aa+1)
print(ans)