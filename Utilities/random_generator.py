import random
while(5!=0):
    x=int(input("Enter First:"))
    y=int(input("Enter Second:"))
    for i in range(8):
        print(random.randint(x,y), end=' ')
    ch=input("Do you wish to Continue?")
    if(ch=="Yes"):
        continue
