from quadratic_roots import roots
def linear_solver(a, b):
    if a==0:
        raise ZeroDivisionError("Bruh. This thing is too advanced for you.")
    else:
        x=(-b)/a
        return x
    
M=str(input("""What equation would you like to solve? This program can solve:
1) Linear
2) Quadratic
3) Solve for x when other variables are given (x+y+z=n)
Please type the first letter of the respective operation you would like to do:""")).lower()
while True:
    
    if M=="l" or "q" or "S":
        break
    else:
        print("You stupid idiot")
if M=="l":
    a=float(input("Enter value of a for equation in format: ax+b=0"))
    b=float(input("Enter value of b for equation in format: ax+b=0"))
    print("The solution for x is:", linear_solver(a, b))
elif M=="q":
    a=float(input("Enter value of a for equation in format: ax^2+bx+c=0"))
    b=float(input("Enter value of b for equation in format: ax^2+bx+c=0"))
    c=float(input("Enter value of c for equation in format: ax^2+bx+c=0"))
    print("The solutions for x are:", quadratic_solver(a, b, c))
else:
    n=int(input("Enter the Constant For The Equation x+y+z=n:"))
    print(f"The Equation Has Become:x+y+z={n}")
    list1=[int(input(f"Enter the Variable {i+1}:")) for i in range(2)]
    print(f"The Answer To The Variable 3 is:{n-sum(list1)}")
