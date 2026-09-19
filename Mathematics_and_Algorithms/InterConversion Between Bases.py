#Changing Base Of Number
def Base_Change(num,base):
    temp=num
    a=[]
    iteration=0
    while(temp!=0):
        newnum=(temp%base)
        temp//=base
        iteration+=1
        a.append(newnum)
    return a[::-1]
def Base_revert(a,originalbase):
    Sum=0
    for i in range(len(a)):
        Sum+=a[i]*(originalbase**(len(a)-i-1))
    return Sum
def Getting_Number(num,base):
    a=Base_Change(num,base)
    print(f"The base {base} representation of The Given Number Is:{a}")
    Base=int(input("Enter The New Base To Which You Want To Convert:"))
    b=Base_Change(Base_revert(a,base),Base)
    print(f"The base {Base} representation Of The Number Above is:{b}")
base=int(input("Enter The Base To Which You want To Convert Your Number:"))
number=int(input(f"Enter The Number For Conversion To Base {base}:"))
list1=Base_Change(number,base)
Getting_Number(number,base)
