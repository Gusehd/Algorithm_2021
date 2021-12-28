#19101185 강동현 알고리즘 Miller-Rabin primality test

def powmod(x, y, m):
    r = 1
    while y > 0:
        if y % 2:
            r = (r * x) % m
        y //= 2
        x = x**2 % m
    return r

def s_and_d(n):
    s=0
    d=0
    nc = n-1
    while True:
        if nc % 2 == 0:
            nc = nc // 2
            s += 1
        else:
            d = nc
            break
    return  s , d

n = int(input())

test = [2,7,61]
s,d = s_and_d(n)
check = 1

if s == 0:
    s = 1

for a in test:
    if (a**d) % n != 1:
        result = True
    else:
        result = False

    for r in range(0,s):
        if powmod(a,(2**r)*d,n) != n-1:
            result = result and True
        else:
            result = result and False

    if result:
        check = 0
        break

print(check)
