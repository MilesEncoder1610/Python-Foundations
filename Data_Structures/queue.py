#Implementation Of Queue#
MyQ=[]
content='''1.Enqueue Operation()
2.Dequeue Operation()
3.Peek Operation()
4.IsFull Check()
5.IsEmpty Check()
6.Size(Queue) Check()
7.Exit'''
def Enqueue(Queue,Ele,Length):
    if(IsFull(Queue,Length)==True):
        return None
    else:
        Queue.append(Ele)
        return True
def Dequeue(Queue):
    if(IsEmpty(Queue)==True):
        print("UnderFlow Error")
        return None
    else:
        Queue.pop(0)
        return True
def Peek(Queue):
    if(IsEmpty(Queue)==True):
        return None
    else:
        return Queue[0]
def IsFull(Queue,Length):
    if(Size(Queue)==Length):
        return True
def IsEmpty(Queue):
    if(Size(Queue)==0):
        return True
    else:
        return False
def Size(Queue):
    return len(Queue)
print(content)
length=int(input("Enter Maximum Number Of Elements You Want To Enter Into The Queue:"))
while True:    
    a=int(input("Enter The Operation You want to Perform:"))
    if(a==1):
        n=int(input("Enter The Element You Want To Insert:"))
        a=Enqueue(MyQ,n,length)
        if(a==True):
            print(f"Element {n} is Successfully Inserted!")
        else:
            print("OverFlow Error!")
    elif(a==2):
        print(f"Eliminating The Element:{Peek(MyQ)}")
        a=Dequeue(MyQ)
        if(a==True):
            print("The Queue Was Not Empty!")
    elif(a==3):
        print(f"The Front Element Is:{Peek(MyQ)}")
        if(Peek(MyQ)==None):
           print("UnderFlow Error")
    elif(a==4):
        print("Checking for OverFlow:")
        a=IsFull(MyQ,length)
        if(a==True):
            print("OverFlow Condition Achieved!!")
        else:
            print(f"No OverFlow; The Size Of The Queue Is:{Size(MyQ)}")
    elif(a==5):
        print("Checking If The Queue Is Empty:")
        a=IsEmpty(MyQ)
        if(a==False):
            print("Not Empty")
        else:
            print("UnderFlow Error; Queue Is Empty!")
    elif(a==6):
        print(f"The Current Size Of The Queue Is:{Size(MyQ)}")
    elif(a==7):
        print("Operations Complete; Exiting from Queue!")
        break
    else:
        print("Enter Valid Number")
