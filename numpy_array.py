arr=np.array([[[1,2],[3,4]],[[7,6],[8,9]]])
print(arr)
print("*"*20)

flat_arr=arr.flatten()
print(flat_arr)
print("*"*20)

##reshapping
arr=np.array([[3,4,5],[6,2,9],[2,10,5],[1,7,9]])
print(arr)
print(arr.shape)
print("*"*20)

reshape_arr=np.reshape(arr,(2,6))
print(reshape_arr)
print(reshape_arr.shape)
print("*"*20)


##splitting
print(np.vsplit(arr,4))               ### vertical split
print("*"*20)

print(np.hsplit(arr,3))                ###horizonally split
print("*"*20)

print(np.split(arr,2  ,axis=0))
print(np.split(arr,3  ,axis=1))
print("*"*20)

####merging the arrays
arr1=np.array([3,4,5])
arr2=np.array([6,2,9])
arr3=np.array([2,10,5])
arr4=np.array([1,7,9])

concat_arr=np.concatenate((arr1,arr2))
print(concat_arr)
print("*"*20)

concat_arr=np.vstack((arr1,arr2,arr3,arr4))
print(concat_arr)
print("*"*20)

concat_arr=np.hstack((arr1,arr2,arr3,arr4))
print(concat_arr)
print("*"*20)

concat_arr=np.stack((arr1,arr2,arr3,arr4),axis=0)
print(concat_arr)
concat_arr=np.stack((arr1,arr2,arr3,arr4),axis=1)
print(concat_arr)
print("*"*20)

arr=np.array([[[1,2,3],[4,5,6]],[[6,3,5],[9,8,7]]])
print(arr)
print("--------------------")


##accesing the specific elements 
print(arr[0][1][1])
print(arr[1,1,2])
print("--------------------")

##accesing the specidic rows
print(arr[0])
print("--------------------")
print(arr[1,:,:])
print("--------------------")
print(arr[:,1,:])
print(arr[:,0,2])
print('------------------')

##accesing eith the specific case
print(arr[[0,1],:,:])
print(arr[[1],:,:-1])
print(arr[[0],1,1:])
print("-----------------")

##accessing with the specific condtitions
print(arr[arr>5])
print(arr[arr==5])
arr[arr>8]=0
print(arr)


##broadcasting the efficient calculation
x=np.array([94,6,4])
y=np.array([[19,26,12],[16,54,10]])
print(x,y)
print("*"*20)

##addition
print(x+y)
print(x+[10])
print("*"*20)

##subtarction
print(x-y)
print(y-6)
print("*"*20)

##multiplication
print(x*y)
print(y*3)
print("*"*20)

##division
print(x/y)
print(y/2)
print("*"*20)

###exponential
print(x**2)
print(y**2)
print("*"*20)

##modulus
print(x%2)
print(y%5)


###comparison between 2 arrays with different dimesions
print(x<y)
print(x>=y)
print(x==y)
print(x!=y)


###logical operators
print(x&y)
print(x|y)
print(x^y)


##bitwise operators
print(np.bitwise_and(x,y))
print(np.bitwise_or(x,y))
print(np.bitwise_not(x,y))
print(np.bitwise_xor(x,y))
print(np.bitwise_right_shift(y,x))


##where clause in array
np.random.seed(10)
arr=np.random.randint(0,12,size=(3,2,3))
print(arr)

indices=np.where(arr>=5)
print(list[indices])
print(arr[indices])
