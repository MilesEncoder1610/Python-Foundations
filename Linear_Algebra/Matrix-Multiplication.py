from Required_Functions import Matrix_Multiplication,Convert_StringMatrix,Manual_Matrix,Random_Matrix
Ans=input("Enter Manual/Random/Convert Matrix:")
if(Ans=="Manual"):
    Matrix1=Manual_Matrix()
    Matrix2=Manual_Matrix()
elif(Ans=="Convert"):
    Matrix1=Convert_StringMatrix()
    Matrix2=Convert_StringMatrix()
else:
    Matrix1=Random_Matrix()
    Matrix2=Random_Matrix()
print(f"The Matrices are:{Matrix1}\n{Matrix2}")
print(f"The Matrix Obtained By The Multiplication:{Matrix_Multiplication(Matrix1,Matrix2)}")
