def roots(a,b,c):
#Discriminant
    w=b**2-4*a*c
    if(w>0):
        w1="The Equation Has 2 Real Roots"
    elif(w==0):
        w1="The Equation Has 2 Equal & Real Roots"
    else:
        w1="The Equation Has No Real Roots"
    print(w1)
    W=w**(1/2)
    Root1=((W-b)/a)/2
    Root2=((-W-b)/a)/2
    return Root1,Root2
a=int(input("Enter x^2 coefficient:"))
b=int(input("Enter x coefficient:"))
c=int(input("Enter constant term:"))
R1,R2=roots(a,b,c)
print("The Roots are:",R1,",",R2)
