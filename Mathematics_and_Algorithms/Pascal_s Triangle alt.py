from math import factorial
k=int(input("Enter The Number of Rows in Pascal's Triangle:"))
for i in range(k+1):
    for j in range(i+1):
        a=factorial(i)
        b=factorial(j)
        c=factorial(i-j)
        print(int(a/(b*c)),end=' ')
    print()
