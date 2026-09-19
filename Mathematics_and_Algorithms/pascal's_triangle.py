def Fact(n):
    fact=1
    if(n==0):
        return fact
    elif(n>0):
        while(n!=0):
            fact*=n
            n-=1
        return fact
k=int(input("Enter The Number of Rows in Pascal's Triangle:"))
for i in range(k+1):
    for j in range(i+1):
        a=Fact(i)
        b=Fact(j)
        c=Fact(i-j)
        print(a/(b*c),end=' ')
    print()
