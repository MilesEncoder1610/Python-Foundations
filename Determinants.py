from Required_Functions import Random_Det,Manual_Det,Convert_StringDet,Determinant
from time import time
Ans=input("Enter Random/Manual/Convert Determinant:")
if(Ans=="Manual"):
    Det=Manual_Det()
elif(Ans=="Convert"):
    Det=Convert_StringDet()
else:
    Det=Random_Det()
print(Det)
a=time()
Determinant_Value=Determinant(Det)
print(f"The Determinant Value is:{Determinant_Value}, being found within {time()-a} seconds!")
