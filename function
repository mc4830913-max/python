###defining a function 
def greet():
    print("hello")
greet()
print([greet() for i in range(10)])      ##comprehensions
for i in range(5):
    greet()
print("*"*30)
g_var=5
def scope():
    l_var=4
    print(l_var,g_var)
print(g_var)   
scope()
print("*"*30)

## this code is reuseable and also used by in other files uisng import suppose file name is data analytics
def summ(a=0,b=0):
    return [a+b,a-b,a*b]
s=summ(23,45)
print(s)
print(type(s))

a=[1,2,3,4,5,6,7]
def sq_li(a):
    return [i**2 for i in a]
def cu_li(a):
    return[i**3 for i in a]
def final_li(a):
    return sq_li(a)+cu_li(a)
def final(a):
    lis_1=sq_li(a)
    lis_2=cu_li(a)
    return [lis_1[i]+lis_2[i] for i in range(len(lis_1))]
------------------------------------------------------------------------------------------------------------------
rom data_analytics import *
##from data_analytics import subm
##from data_analytics import arithemetic
##from data_analytics import sqr
##from data_analytics import cu
print(greet("monu"))
print(subm(12,15))
print(arithemetic(98,45))
print(sqr([3,4,5,8,2]))
print(cu([3,4,5,8,2]))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(final(list1,list2))
print("*"*40)




