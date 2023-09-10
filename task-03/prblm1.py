cdef sumodd(l):
    sum1=0
    for i in l:
        if i%2!=0:
            sum1+=i
    print("The sum of odd no. in the list is:",sum1)
#main
lis=[]
n=int(input("Enter the no. of elements:"))
for i in range(n):
    e=int(input("Enter the elements in the list:"))
    lis.append(e)
sumodd(lis)
    

