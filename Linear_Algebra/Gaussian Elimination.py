from random import random
list1=[]
n=int(input("Enter the N for N x N Determinant: "))
for i in range(n):
    list2=[]
    for j in range(n):
        list2.append(int(random()*100))
    list1.append(list2)
print(list1)
for i in range(n-1,0,-1):
    for j in range(i):
        list3=[]
        for k in range(n):
            list3.append((list1[j][k]*list1[i][i]-list1[j][i]*list1[i][k])/list1[i][i])
        list1[j]=list3
for i in list1:
    print(i)
Det=1
for i in range(n):
    Det*=list1[i][i]
    if(Det==0):
        break
print(Det)
