#Implementation Of Deque#
MyQ=[]
content='''1.InsertRear Operation()
2.InsertFront Operation()
3.DeletionRear Operation()
4.DeletionFront Operation()
5.GetFront Operation()
6.GetRear Operation()
7.IsFull Check()
8.IsEmpty Check()
9.Size(Deque) Check()
10.Exit'''
def InsertionRear(Deque,Ele,Length):
    if(IsFull(Deque,Length)==True):
        return None
    else:
        Deque.append(Ele)
        return True
def InsertionFront(Deque,Ele,Length):
    if(IsFull(Deque,Length)==True):
       return None
    else:
        Deque.insert(0,Ele)
        return True
def DeletionRear(Deque):
    if(IsEmpty(Deque)==True):
        print("UnderFlow Error")
        return None
    else:
        Deque.pop()
        return True
def DeletionFront(Deque):
    if(IsEmpty(Deque)==True):
        print("UnderFlow Error")
        return None
    else:
        Deque.pop(0)
        return True
def GetFront(Deque):
    if(IsEmpty(Deque)==True):
        return None
    else:
        return Deque[0]
def GetRear(Deque):
    if(IsEmpty(Deque)==True):
        return None
    else:
        return Deque[-1]
def IsFull(Deque,Length):
    if(Size(Deque)==Length):
        return True
def IsEmpty(Deque):
    if(Size(Deque)==0):
        return True
    else:
        return False
def Size(Deque):
    return len(Deque)
print(content)
length=int(input("Enter Maximum Number Of Elements You Want To Enter Into The Deque:"))
while True:    
    a=int(input("Enter The Operation You want to Perform:"))
    if(a==1):
        n=int(input("Enter The Element You Want To Insert To The Rear End:"))
        a=InsertionRear(MyQ,n,length)
        if(a==True):
            print(f"Element {n} is Successfully Inserted!")
        else:
            print("OverFlow Error!")
    elif(a==2):
        n=int(input("Enter The Element You Want To Insert To The Front End:"))
        a=InsertionFront(MyQ,n,length)
        if(a==True):
            print(f"Element {n} is Successfully Inserted!")
        else:
            print("OverFlow Error!")
    elif(a==3):
        print(f"Eliminating The Rear Element:{GetRear(MyQ)}")
        a=DeletionRear(MyQ)
        if(a==True):
            print("The Deque Was Not Empty!")
    elif(a==4):
        print(f"Eliminating The Front Element:{GetFront(MyQ)}")
        a=DeletionFront(MyQ)
        if(a==True):
            print("The Deque Was Not Empty!")
    elif(a==5):
        print(f"The Front Element Is:{GetFront(MyQ)}")
        if(GetFront(MyQ)==None):
           print("UnderFlow Error")
    elif(a==6):
        print(f"The Rear Element Is:{GetRear(MyQ)}")
        if(GetFront(MyQ)==None):
           print("UnderFlow Error")
    elif(a==7):
        print("Checking for OverFlow:")
        a=IsFull(MyQ,length)
        if(a==True):
            print("OverFlow Condition Achieved!!")
        else:
            print(f"No OverFlow; The Size Of The Deque Is:{Size(MyQ)}")
    elif(a==8):
        print("Checking If The Deque Is Empty:")
        a=IsEmpty(MyQ)
        if(a==False):
            print("Not Empty")
        else:
            print("UnderFlow Error; Deque is Empty")
    elif(a==9):
        print(f"The Current Size Of The Deque Is:{Size(MyQ)}")
    elif(a==10):
        print("Operations Complete; Exiting from Deque!")
        break
    else:
        print("Enter Valid Number")
