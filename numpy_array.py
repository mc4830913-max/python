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
