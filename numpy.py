import numpy as np
import time
lst=[1,2,3]
print(lst)
print(type(lst))



arr=np.array([1,2,3])
print(arr)
print(type(arr))



print(arr==lst)
print(arr.tolist()==lst)


# # ### adding elements in an array vs list

print(lst)
lst.append(4)
print(lst)
print("--------")

print(arr)
arr=np.append(arr,4)
print(arr)
print("---------")

# # ###pop the lements from array vs list

print(lst)
lst.pop()
print(lst)
print("--------")

print(arr)
arr=np.delete(arr,2)
print(arr)
print("---------")



# # ###updating the elments 
print(lst)
lst[2]=9
lst[1]=8
print(lst)
print('-----')


print(arr)
arr[2]=9
arr[1]=8
print(arr)
print('------')



###array vs list comparrison
##creating list nad array
my_lst=list(range(10000000))
my_array=np.arange(10000000)


#search for a list 
start_time=time.time()
for _ in range(500):
    if 5000000 in my_lst:
        pass
end_time=time.time()
print(end_time-start_time)    


#search for a array 
start_time=time.time()
for _ in range(500):
    if 5000000 in my_array:
        pass
end_time=time.time()
print(end_time-start_time) 



lst=[4,5,6,8,2]
print(lst)
lst1=lst.copy()
print(lst1)



# ##creating 2d array
arr=np.array([['1','2','3'],['3','4','5']])
print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.size)
print(type(arr))
print(arr.itemsize)
print("***************")

# #creatind 3d array
arr_=np.array([[[1,2,3],[3,4,5]],
              [[1,2,3],[3,4,5]]
               ,[[1,2,3],[3,4,5]]])
print(arr_)
print(arr_.shape)
print(arr_.dtype)
print(arr_.size)
print(type(arr_))
print(arr_.itemsize)


##copy function in lists
lst=[4,5,6,8,2]
print(lst)

lst1=lst
print(lst1)
print("**********************")

lst[2]=20
print(lst)
print(lst1)
print("**********************")

del(lst[0])
print(lst)
print(lst1)
print("**********************")

lst=[4,5,6,8,2]
print(lst)
lst1=lst.copy()
print(lst1)
print("**********************")

lst[1]=3
print(lst)
print(lst1)
print("**********************")


###copy function in arrays
arr=np.array([4,5,6,8,2])
print(arr)
arr_=arr.copy()
print(arr_)

arr[3]=10
print(arr)
print(arr_)


arr=np.zeros((3,4,5),dtype=int)
print(arr)


arr=np.ones((3,4,5),dtype=int)
print(arr)


arr=np.eye((5),dtype=int)
print(arr)


##random number generator
arr=np.random.rand(2,3)
print(arr)

arr=np.random.randint(low=10,high=50,size=(5,5))
print(arr)

arr=np.random.uniform()
print(arr)


arr=np.random.randint(low=1,high=50,size=100)
for i in range(1,10):
    print(i,arr.tolist().count(i))


###managing random with seeds
np.random.seed(5)
print(np.random.rand())
print(np.random.rand(10))
print(np.random.rand(3,4))
arr=np.random.randint(2,size=100)
print(len(arr[arr==1]))
print(len(arr[arr==0]))


for i in range(10):
    arr=np.random.randint(2,size=1000)
    print(len(arr[arr==1]),len(arr[arr==1]))





