#Implementation Of Stack#
GlassStack=[]
content='''1.Push Operation()
2.Pop Operation()
3.Peek Operation()
4.Overflow Check()
5.IsEmpty Check()
6.Size(Stack) Check()
7.Exit'''
from Required_Functions1 import Push1 as Push,Pop1 as Pop,Peek,OverFlow,IsEmpty,Size
print(content)
length=int(input("Enter Maximum Number Of Elements You Want To Enter Into The Stack:"))
while True:    
    a=int(input("Enter The Operation You want to Perform:"))
    if(a==1):
        n=int(input("Enter The Element You Want To Insert:"))
        a=Push(GlassStack,n,length)
        if(a==True):
            print(f"Element {n} is Successfully Pushed!")
        else:
            print("OverFlow Error!")
    elif(a==2):
        print(f"Eliminating The Element:{Peek(GlassStack)}")
        a=Pop(GlassStack)
        if(a==True):
            print("The Stack Was Not Empty!")
    elif(a==3):
        print(f"The Top Element Is:{Peek(GlassStack)}")
        if(Peek(GlassStack)==None):
           print("UnderFlow Error")
    elif(a==4):
        print("Checking for OverFlow:")
        a=OverFlow(GlassStack,length)
        if(a==True):
            print("OverFlow Condition Achieved!!")
        else:
            print(f"No OverFlow; The Size Of The Stack Is:{Size(GlassStack)}")
    elif(a==5):
        print("Checking If The Stack Is Empty:")
        a=IsEmpty(GlassStack)
        if(a==False):
            print("Not Empty")
        else:
            print("UnderFlow Error; Stack Is Empty!")
    elif(a==6):
        print(f"The Current Size Of The Stack Is:{Size(GlassStack)}")
    elif(a==7):
        print("Operations Complete; Exiting from Stack!")
        break
    else:
        print("Enter Valid Number")
