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


-----------------------------------------------------------------------------------------------------------------------
#student marksheet 
import math
student=str(input("enter your name:"))
math=int(input("enter the marks in math:"))
English=int(input("enter the marks in English:"))
Hindi=int(input("enter the marks in Hindi:"))
total=math,Hindi,English
avg=(math+Hindi+English)/3
print("student:",student)
print("Total marks :",sum(total))
print("Avergae :",avg)
if avg>=90:
    print("Grade :A")
elif avg>=75 and avg<90: 
    print("Grade :B")
elif avg>=50 and avg<75:
    print("Grade :C")
else :
    print("Fail")

#hidden reward
t=[2,4,6,8,10,12,14]
num=int(input("enter the number:"))
if num in t:
    print("you won")
else:
    print("try again")


#password checking 
password=input("enter the password:")
hasupper=False
haslower=False
hasdigit=False
special=False
for ch in password:
    if ch.isupper():
        hasupper=True
    
    if ch.islower():
        haslower=True
       
    if ch.isdigit():
        hasdigit=True
    if ch in "@#$%!":
        special=True
if len(password)>=8 and hasupper and haslower and hasupper and special:
    print("strong password")
else:
 print("weak password")
    
        


print(final(list1,list2))
print("*"*40)




