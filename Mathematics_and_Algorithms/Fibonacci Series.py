from time import time
def Fibo(n):
    Fibo=[0,1]
    if(n<2):
        return Fibo[0:n]
    else:
        for i in range(n-2):
            b=Fibo[i+1]+Fibo[i]
            Fibo.append(b)
        return Fibo
n=int(input("Enter the Number Of Fibonacci Numbers You Want:"))
a=time()
FiboList=Fibo(n)
for i in range(len(FiboList)):
    print(f"The Number {i+1} is:{FiboList[i]}")
print(f"The Time Taken By The Loop is:{time()-a}")
