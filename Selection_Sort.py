def Selection_sort(List1):
    for i in range(len(List1)-1):
        Min=List1[i]
        for j in range(i+1,len(List1)):
            if(List1[j]<Min):
                Min=List1[j]
            else:
                continue
        List1[i+List1[i:].index(Min)],List1[i]=List1[i],List1[i+List1[i:].index(Min)]
    return List1
from random import random
n=int(input("Enter the Number of Elements You Want To See:"))
List1=[int(100*random()) for i in range(n)]
print(List1)
print(f"The Sorted List You Want Is:{Selection_sort(List1)}")
#Usage Of Complex Indices In Accurate Manner
#See This For Better Revision
