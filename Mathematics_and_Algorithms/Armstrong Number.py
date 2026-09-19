a=int(input("Enter The Number:"))
Sum=0
temp=a
while(a!=0):
    r=a%10
    Sum=Sum+r**3
    a=a//10
if(temp==Sum):
    print("This Is An Armstrong Number!")
else:
    print("This Is Not An Armstrong Number!")
    
