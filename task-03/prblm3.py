for _ in range(int(input())):
    x=int(input())
    sum1=0
    for i in range(x):
        if i%3==0 or i%5==0:
            sum1+=i
    print(sum1)
