def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l=[]
    if is_prime(n):
        print(n)
    else:
        for i in range(2,n//2+1):
            if n%i==0 and is_prime(i):
                l.append(i)
        print(l[-1])
                
