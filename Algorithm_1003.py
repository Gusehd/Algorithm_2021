#19101185 강동현 - Fibona-chicken

inNum=int(input(""))
inNum=int(inNum)

def getFibonacciList(num):
    i=0
    hwm = 0
    fn = [1,1]
    while hwm < int(num):
        hwm = fn[i] + fn[i+1]
        if hwm < int(num):
            fn.append(hwm)
            i = i + 1
    return fn;

def getZeken(f):
    i = 0
    s = 0
    idx = []
    f.reverse()
    cnt = len(f)-1
    for i in f:
        if (i+s <= inNum):
          s = i + s
          idx.append(cnt)
          cnt -= 1
        else:
          cnt -= 1
    return idx;

fiboNum = getFibonacciList(inNum)
stack = getZeken(fiboNum)
ans = 0
fiboNum.reverse()
for i in stack:
  if i == 0:
    ans += 1
  else:
    ans += fiboNum[i-1]
print(ans)