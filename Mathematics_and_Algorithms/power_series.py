def Power_Series(num,exp):
    from math import log,factorial
    from time import time
    import pandas as pd
    expo=[float(f"{(i+1)*0.01:.2f}") for i in range(int(100*exp))]
    file=open("Power Series_Steps.txt","w")
    file.close()
    dict1={}
    dict2={}
    f=time()
    try:
        for d in expo:
            c=[]
            for j in range(1,num+1):
                x=log(j)*d
                a=[1]
                i=1
                while (i>=0):
                    sum1=sum(a)
                    b=(x**i)/factorial(i)
                    a.append(b)
                    if(sum1==sum(a)):
                        c.append(i)
                        break
                    else:
                        i+=1
            b=[]
            for i in range(1,max(c)+1):
                a=c.count(i)
                b.append(a)
            with open("Power Series_Steps.txt","a") as file:
                file.write(f"\nList1 of Exponent {d} is:")
                file.write(str(c))
                file.write("\nThe Tally Of The Steps Involoved:")
                file.write(str(b))
            dict1[d]=[b.index(max(b))+1,max(b)]
            dict2[d]=b.index(max(b))+1
    except OverflowError:
        print("The Number Is Too Large:")
    finally:
        with open("Power Series_Steps.txt","a") as file:
            file.write(f"\nThe Set Of all Exponents,The Average Steps and The Number Of Such Occurances is:{dict1}")
            file.write(f"\nSpecial Dictionary:{dict2}")
        print(f"The Program Ends:{time()-f}")
        df1=pd.DataFrame(dict2,index=[0])
        print(df1)
        df1.to_excel('Power_Series.xlsx')
list1=Power_Series(int(input("Enter The Base Of Required Number:")),float(input("Enter The Exponents Of Required Number:")))
