def Bubble_Sort(List1):
    for i in range(len(List1)-1):
        for j in range(len(List1)-i-1):
            if(List1[j]>List1[j+1]):
                List1[j],List1[j+1]=List1[j+1],List1[j]
    return List1
n=int(input("Enter The Number Of Elements You Want To Enter:"))
a=Bubble_Sort([int(input("Enter The Numerical element:")) for i in range(n)])
print(f"The Sorted List is:{a}")
