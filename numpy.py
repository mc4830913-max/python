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




