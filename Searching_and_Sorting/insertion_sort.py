#InsertionSorting
def Insertion_Sort(list1):
    for i in range(1,len(list1)):
        for j in range(i,0,-1):
            if(list1[j]<list1[j-1]):
                list1[j],list1[j-1]=list1[j-1],list1[j]
            else:
                break
    return list1
from random import random
n=int(input("Enter The Number Of Entries In List:"))
List1=[int(100*random()) for i in range(n)]
print(f"The Sorted List is:{Insertion_Sort(List1)}")
new=[]
for i in range(max(List1)):
    new.append(List1.count(i))
print(max(new),new.index(max(new)))
