#Required Set Of Functions
def Peek(Stack):
    if(IsEmpty(Stack)==True):
        return None
    else:
        return Stack[-1]
def Pop1(Stack):
    if(IsEmpty(Stack)==True):
        print("UnderFlow Error")
        return None
    else:
        Stack.pop()
        return True
def Push1(Stack,Ele,Length):
    if(OverFlow(Stack,Length)==True):
        return None
    else:
        Stack.append(Ele)
        return True
def OverFlow(Stack,Length):
    if(Size(Stack)==Length):
        return True
def IsEmpty(Stack):
    if(Size(Stack)==0):
        return True
    else:
        return False
def Size(Stack):
    return len(Stack)
