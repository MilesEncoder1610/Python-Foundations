#Hash Searching Multiple
from random import random
n=int(input("Enter The Number Of Entries You Want In The List:"))
e=int(input("Enter The Value for the number of digits of number in List:"))
list1=[int((10**e)*random()) for i in range(n)]
def Sort(list1):
    temp=list1
    list1=[]
    for i in range(len(temp)):
        list1.append(min(temp))
        temp.pop(temp.index(min(temp)))
    return list1
list1=Sort(list1)
print(f"The Sorted List is:{list1}")
key=int(input("Enter The Number You Want To Search From List:"))
def Hash(list1,key):
    temp1=list1
    for j in range(len(str(max(list1)))):
        newlist=[]
        for i in range(10):
            newlist.append(list())
        for k in temp1:
            c="0"*j+str(k)
            dig=int(c[-1-j])
            newlist[dig].append(k)
        a="0"*j+str(key)
        b=int(a[-1-j])
        if(len(newlist[b])==0):
            print("No such Number Exists!")
            temp1=[]
            break
        else:
            temp1=newlist[b]
    return len(temp1)
def index_num(list1,key):
    if(Hash(list1,key)==0):
        print("No Index Found!")
        return None
    else:
        index=0
        for i in list1:
            if(i==key):
                index+=1
                break
            else:
                index+=1
        return index
print(f"The Number of Occurances of {key} in the list is: {Hash(list1,key)}")
print(f"The First Occurance is at Position={index_num(list1,key)}")
