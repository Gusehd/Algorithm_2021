#19101185 강동현 알고리즘 - Approximate Clustering ( K - Means Clustering )

import sys
import math

n,k = map(int , sys.stdin.readline().split(" "))
stack = []
for o in range(n):
    stack.append(list(map(int , sys.stdin.readline().split(" "))))
    stack[o].append(o)
c = [stack[0]]
d = [0 for i in range(n)]

def way(x1,y1,x2,y2):
    a = x1 - x2
    b = y1 - y2
    return math.sqrt((a * a) + (b * b))

for j in range(2,k+1):
    cl_xx = 0
    cl_yy = 0
    cl_zz = 0
    maxx = 0
    for i in range(0,n):
        if i not in c:
            w = math.inf
            cl_x = 0
            cl_y = 0
            cl_z = 0
            for p in c:
                way_cl = way(stack[i][0],stack[i][1],p[0],p[1])
                if w > way_cl:
                    cl_x = stack[i][0]
                    cl_y = stack[i][1]
                    cl_z = stack[i][2]
                    w = way_cl

            if maxx < w:
                maxx = w
                cl_xx = cl_x
                cl_yy = cl_y
                cl_zz = cl_z
    c.append([cl_xx,cl_yy,cl_zz])
c.sort(key=lambda x : x[2])

for i in c:
    print("%d %d" %(i[0],i[1]))


