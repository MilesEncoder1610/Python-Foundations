def Random_Matrix():
    rows=int(input("Enter The Number Of Rows In Matrix:"))
    columns=int(input("Enter The Number Of Columns In Matrix:"))
    from random import random
    Matrix=[]
    n=int(input("Enter The Number Of Digits You Want:"))
    for i in range(rows):
        row=[]
        for j in range(columns):
            row.append(int(random()*10**n))
        Matrix.append(row)
    return Matrix
def Random_Det():
    n=int(input("Enter The Number Of Rows/Columns for Determinant:"))
    from random import random
    Det=[]
    n1=int(input("Enter The Number Of Digits You Want:"))
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(int(random()*10**n1))
        Det.append(row)
    return Det
def Manual_Matrix():
    Matrix=[]
    n=int(input("Enter the Number Of Rows:"))
    m=int(input("Enter the Number Of Columns:"))
    for j in range(n):
        Ele=[]
        for i in range(m):
            Ele.append(int(input(f"Enter The Element of Row {j+1},Column {i+1}:")))
        Matrix.append(Ele)
    return Matrix
def Manual_Det():
    Det=[]
    n=int(input("Enter the Number Of Rows/Columns:"))
    for j in range(n):
        Ele=[]
        for i in range(n):
            Ele.append(int(input(f"Enter The Element of Row {j+1},Column {i+1}:")))
        Det.append(Ele)
    return Det 
def Convert_StringMatrix():
    Matrix1=input("Enter The StringMatrix:")
    temp=Matrix1
    Matrix=[[] for i in range(temp.count("[")-1)]
    rowcount=0
    for i in range(1,len(temp)-1):
        if(temp[i]=="["):
            j=i+1
            while(temp[j]!="]"):
                if(temp[j].isdigit()):
                    k=j
                    num=""
                    while(temp[k] not in ",]"):
                        num+=temp[k]
                        k+=1
                    Matrix[rowcount].append(int(num))
                    j=k
                else:
                    j+=1
            rowcount+=1
    return Matrix
def Convert_StringDet():
    Det1=input("Enter The StringMatrix for Determinant:")
    temp=Det1
    Det=[[] for i in range(temp.count("[")-1)]
    rowcount=0
    for i in range(1,len(temp)-1):
        if(temp[i]=="["):
            j=i+1
            while(temp[j]!="]"):
                if(temp[j].isdigit()):
                    k=j
                    num=""
                    while(temp[k] not in ",]"):
                        num+=temp[k]
                        k+=1
                    Det[rowcount].append(int(num))
                    j=k
                else:
                    j+=1
            rowcount+=1
    return Det
def Transpose(Matrix):
    a=[]
    for i in range(len(Matrix[0])):
        b=[]
        for j in range(len(Matrix)):
            c=Matrix[j][i]
            b.append(c)
        a.append(b)
    return a
def Matrix_Multiplication(Matrix1,Matrix2):
    Matrix2=Transpose(Matrix2)
    if(len(Matrix1[0])!=len(Matrix2[0])):
        print("The Multiplication is Not Possible!")
        return None
    else:
        a=[]
        for i in Matrix1:
            b=[]
            for j in Matrix2:
                Sum=0
                for k in range(len(Matrix1[0])):
                    Sum+=i[k]*j[k]
                b.append(Sum)
            a.append(b)
        return a
def Cofactor_ListOutput(Matrix,k):
    temp=Matrix[1:]
    List1=[[] for l in range(len(temp))]
    for a in range(len(temp)):
        for b in range(len(temp[a])):
            if(b!=k):
                List1[a].append(temp[a][b])
    return List1
def Cofactor_detValue(Matrix,k):
    temp=Matrix[1:]
    List1=[[] for l in range(len(temp))]
    for a in range(len(temp)):
        for b in range(len(temp[a])):
            if(b!=k):
                List1[a].append(temp[a][b])
    return Determinant(List1)*(-1)**k
def Determinant(det):
    if(len(det)==2):
        return det[0][0]*det[1][1]-det[1][0]*det[0][1]
    else:
        return sum([(-1)**i*det[0][i]*Determinant(Cofactor_ListOutput(det,i)) for i in range(len(det))])
