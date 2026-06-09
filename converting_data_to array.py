import numpy as np

#converting tuple into array

tup=(2,3,4,5,6,7)
print(tup)
print(type(tup))
print('-----')

arr=np.array(tup)
print(arr)
print(type(arr))


#converting list into array
lst=[2,3,4,5,6,7]
print(lst)
print(type(lst))
print('-----')

arr=np.array(lst)
print(arr)
print(type(arr))



# #converting dict into array
dct={1:'apple',2:'bananan',3:'mango',4:'orange'}
print(dct)
print(type(dct))
print('-----')

arr=np.array(dct)
print(arr)
print(type(arr))

arr_k=np.array(list(dct.keys()))
arr_v=np.array(list(dct.values()))
print(arr_k)
print(arr_v)


# #converting set into array
set={2,3,4,5,6,2}
print(set)
print(type(set))
print('-----')

arr=np.array(set)
print(arr)
print(type(arr))
print('--------')

# #converting string into array
arr=np.array(list('hello world'))
print(arr)
print(type(arr))
print('--------')



### creating array of intergers 
arr=np.array([3,4,5,0,6])
print(arr)

arr_=arr.astype(float)
print(arr_)

arr_=arr.astype(str)
print(arr_)

arr_=arr.astype(bool)
print(arr_)

print('--------')

### creating array of float

arr=np.array([3.7,4.8,5.0,0.5,6.77])
print(arr)

arr_=arr.astype(int)
print(arr_)

arr_=arr.astype(str)
print(arr_)

arr_=arr.astype(bool)
print(arr_)
print('-----')


### creating array of string
# arr=np.array(["monika","rahul","naina","preet","isha"])
arr=np.array(['1','4','8','9'])
print(arr)

arr_=arr.astype(int)
print(arr_)

arr_=arr.astype(float)
print(arr_)

arr_=arr.astype(bool)
print(arr_)


### creating array of boolean
arr=np.array([False,True,False,True])
print(arr)

arr_=arr.astype(int)
print(arr_)

arr_=arr.astype(float)
print(arr_)

arr_=arr_.astype(str)
print(arr_)