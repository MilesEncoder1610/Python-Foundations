def Linear_Search(List1,key):
    for i in range(len(List1)):
        if(List1[i]==key):
            return i+1
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
a=Linear_Search(List1,key)
print(f"The Element {key} was Found at Position: {a} in The List")
print(f"The Element {key} has appeared in The List for {List1.count(key)} times!")
