import numpy as np
import time

arr=np.array([1,2,3,None,7,8,9,None])
arr[arr==None]=np.nan
for i in range(len(arr)):
    print(i,arr[i])
    
arr=np.array([1,2,3,np.nan,7,8,9,np.nan])    
print(np.isnan(arr))    
print(arr[np.isnan(arr)])  
print(~np.isnan(arr))  
print(arr[~np.isnan(arr)])  


##filling the null with fixesd values 
arr[np.isnan(arr)]=0
print(arr)

##fillng the null values with average
arr=np.array([1,2,3,np.nan,7,8,9,np.nan])
print(arr)
arr[np.isnan(arr)]=np.nanmean(arr)
print(arr)

#creating the matrix
np.random.seed(10)
arr=np.random.randint(1,30,size=(5,5))
print(arr)

##filter elemnet grater then 5
print(arr[arr>5])

##filter elenment that are multiple of 2
print(arr[arr%2==0])

##filter the elemenst both condition satisfy
print(arr[(arr>5) & (arr%2==0)])

##filter the elements that are both divisible by the 3 and 7
print(arr[(arr%3==0) | (arr%7==0)])


##filter the element based on the another ways
arr1=np.array([True,False,True,True,True])
print(arr[arr1])
print("---------------")

print(arr[arr[:,2]>5])

###agrregation function
x=np.array([3,5,8,12,5,6])
print(np.sum(x))

y=np.array([[3,4,7],[8,4,9]])
print(y)
print(np.sum(y, axis=0))
print(np.sum(y, axis=1))

##mean
x=np.array([3,5,8,12,5,6])
print(np.mean(x))

y=np.array([[3,4,7],[8,4,9]])
print(y)
print(np.mean(y,axis=0))
print(np.mean(y,axis=1))

##max
x=np.array([3,5,8,12,5,6])
print(np.max(x))

y=np.array([[3,4,7],[8,4,9]])
print(y)
print(np.max(y,axis=0))
print(np.max(y,axis=1))

np.random.seed(10)
arr=np.random.randint(low=2,high=100, size=50)
print(arr)

mean=np.mean(arr)
median=np.median(arr)
# mode=np.mode(arr)
var=np.var(arr)
std_dev=np.std(arr)

q1=np.percentile(arr,25)
q2=np.percentile(arr,50)
q3=np.percentile(arr,75)

iqr=q3-q1

skewness=np.mean((arr-mean)**3/(std_dev**3))
kutorsis=np.mean((arr-mean)**4/(std_dev**4))

print("mean           :",mean)
print("medain         :",median)
print("var            :",var)
print("std            :",std_dev)
print("quardant1      :",q1)
print("quardant2      :",q2)
print("quardant       :",q3)
print("igr            :",iqr)
print("skeness        :",skewness)
print("kutosis        :",kutorsis)

###serching and sorting
arr=np.array([1,3,5,6,7,8,9,0,3,4,5,6,7])
print(arr)

##linear search
index=np.where(arr==6)[0]
print(index)

##binary search
index1=np.searchsorted(arr,3)
print(index1)

##binary search with multiple value
index1=np.searchsorted(arr,[3,5])
print(index1)

##serching the closesets value
index2=np.argmin(abs(arr-11))
print(index2)

##sorting
###quick sort
sorted_arr=np.sort(arr)
print(sorted_arr)

##quick sort
sorted_arr=np.sort(arr,kind="quicksort")
print(sorted_arr)

##heap sort
sorted_arr=np.sort(arr,kind="heapsort")
print(sorted_arr)

##merge sort
sorted_arr=np.sort(arr,kind="mergesort")
print(sorted_arr)

sorted_arr=np.sort(arr,kind="stablesort")
print(sorted_arr)

import numpy as np

data = np.array(["apple", "banana", "apple", "orange", "banana", "apple"])

unique_items, counts = np.unique(data, return_counts=True)

print("Unique elements:", unique_items)
print("Counts:", counts)



