n=int(input("Enter the Constant For The Equation x+y+z=n:"))
print(f"The Equation Has Become:x+y+z={n}")
list1=[int(input(f"Enter the Variable {i+1}:")) for i in range(2)]
print(f"The Answer To The Variable 3 is:{n-sum(list1)}")
