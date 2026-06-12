import numpy as np
import time

##matrix multiplication
x=np.array([2,3])
y=np.array([7,8])
arr=np.dot(x,y)
arr_=np.cross(x,y)

print(arr,arr_)

a=np.array([[7,6],[3,4]])
b=np.array([[5,4],[2,1]])
print(a,b)
product=np.matmul(a,b)
print(product)
product_=np.dot(b,a)
print(product_)

##determinant
determinant=np.linalg.det(a)
print(determinant)

X=np.array([[1,2,1],[4,5,6,],[2,3,4]])
print("determinant:",np.linalg.det(X))

##transpose
print(X)
print("transpose:",np.transpose(X))

##inverse of a matrix
print(X)
print("inverse:",np.linalg.inv(X))

###system of linear equation
A=np.array([[1,2],[3,4]])
B=np.array([[4],[6]])
print(B.shape)
print("this is the value of linear euation of x and y :",np.linalg.solve(A,B))

##eigion value and eign vector
A=np.array([[5,4],[1,2]])
eignval,eignvect=np.linalg.eig(A)
print(eignval)
print(eignvect)


###saving the dat files
arr=np.array([[1,2,3,],[89,25,43]])
np.savetxt("data.text",arr,delimiter=",")

# np.save("data.npy",arr)      this is used for the jupyter notebook
np.savetxt("dataset.csv",arr,delimiter=",",header="a,b,c")

np.savetxt("jsonn.json",arr,delimiter=",",header="{data :  [",footer="] }")
np.savetxt("data_of_yml.yaml",arr,delimiter=",",header="-data:")
