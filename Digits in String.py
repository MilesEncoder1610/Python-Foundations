str1=input("Enter a string:")
def Digit_count(str1):
    for i in str1:
        cnt=0
        if i.isdigit():
            cnt+=1
            break
    print("The string contains at least one digit." if(cnt==1) else "The string does not contain any digits.")
Digit_count(str1)
