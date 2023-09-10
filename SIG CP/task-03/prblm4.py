import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l=[1,2]
    i=2
    while i<=n:
        i=l[-1]+l[-2]
        l.append(i)
    sum1=0
    print(l)
    for j in l:
        if j%2==0:
            sum1+=j
    print(sum1)
