def Letter_Search(List1,key):
    List2=List1
    temp=[]
    for j in range(len(key)):
        for i in List1:
            if(i[j]==key[j]):
                temp.append(i)
        List1=temp
        temp=[]
    if(len(List1)==1):
        return List2.index(List1[0]),True
    else:
        return None,False
List1=[input("Enter A Word:") for i in range(int(input("Enter the Number Of Elements You Want To Add:")))]
print(f"The List Is:{List1}")
key=input("Enter Word To Check Whether it is Present Or Not:")
a,b=Letter_Search(List1,key)
if(b is True):
    print(f"The Element {key} is Present at Position {a+1}!")
else:
    print(f"The Element {key} Is not Present!")
