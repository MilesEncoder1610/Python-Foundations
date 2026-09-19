num=int(input("Enter The Decimal Number To Convert to Base n Number:"))
n=int(input("Enter the Base:"))
def Power(num,n):
    for i in range(num):
        rem=num%(n**i)
        if(rem==num):
            return i-1
        else:
            continue
a=Power(num,n)
print(a)
def Mod_Division(num,a,n):
    Basen=0
    for j in range(a,-1,-1):
        Basen+=(num//(n**j))*(10**j)
        num%=n**j
    return Basen
Basen=Mod_Division(num,a,n)
print("The Base n Number Representation is:",Basen)
