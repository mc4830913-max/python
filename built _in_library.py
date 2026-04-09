import math
x=10.23
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print("*"*40)

x=4
print(math.exp(x))
print(math.log10(x))
print("*"*40)

x=90
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print("*"*40)

print(math.pi)
print(math.e)
print(10,math.factorial(10))
print("*"*40)

import random
random.seed(40)
print(random.random())
print(random.randint(1,11))
print(random.choice([1,2,3,4,5]))
print(random.sample([1,2,3,4,5],2))
print(random.uniform(1.2,3.4))
print("*"*40)

import datetime
print(datetime.datetime.now())
print(datetime.datetime(2023,10,28,10,30,0))

print(datetime.datetime.now().strftime("%d/%m/%y  %H:%M:%S"))   ##changing the format of date and time

date_1=datetime.datetime(2023,10,28,10,30,0)
date_2=datetime.datetime.now()
print(date_1  - date_2)
print("*"*40)

from collections import Counter, defaultdict,OrderedDict
lst1=[1,2,3,4,5,6,7,4,6,8,9,]
lst2=['a','n','c']
print(Counter(lst1))
print(OrderedDict(enumerate(lst2)))
print("*"*40)

d=defaultdict(int)
d['a']+=2
print(d)
print("*"*40)

d=OrderedDict()
d['one']=2
d['two']=1
print(d)
print("*"*40)

import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print("*"*40)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print("*"*40)

print(string.punctuation)
