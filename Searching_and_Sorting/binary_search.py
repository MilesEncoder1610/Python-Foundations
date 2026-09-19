def Binary_Search(List1,key):
    First=0
    Last=len(List1)-1
    while(First<=Last):
        mid=(First+Last)//2
        if(List1[mid]==key):
            return mid+1
        elif(List1[mid]>key):
            Last=mid-1
        else:
            First=mid+1
def Sort(List1):
    temp=[]
    for i in range(len(List1)):
        temp.append(min(List1))
        List1.remove(min(List1))
    return temp
from random import random
List1=Sort([int(100*random()) for i in range(int(input("Enter The Maximum Numbers you want to Insert:")))])
print("The List is:",List1)
key=int(input("Enter The Number You Want To Search:"))
a=Binary_Search(List1,key)
print(f"The Element {key} was Found at Position: {a} in The List")
