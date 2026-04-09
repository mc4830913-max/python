2nd pattern
num=3
for i in range(1,num+1):
    print(" "*(num-i)+"*"*i+"*"*(i-1))
for k in range(num,0,-1):
    print(" "*(num-k)+"*"*k+"*"*(k-1))

//6th pattern
num=15
for i in range(1,num):
    print(" "*i+"*")
print("*"*(num+1))
for k in range(1,num):
     print(" "*k+"*")
//7th pattern
num=15
for i in range(1,num):
    print(" "*(2*(num-i))+"*"*i)
for k in range(num,0,-1):
     print(" "*(2*(num-k))+"*"*k)

//8th pattern
num=6
print("*"*(num+6))
for i in range(1,num):
    print(" "*(i%num)+"*"+" "*(num+4)+"*")
print(" "*num+"*"*(num+6))

//9th pattern
num=6
print("*"*(num+6))
for i in range(1,num):
    print("*"+" "*(num+4)+"*")
print("*"*(num+6))

//10th pattern
num=6
for i in range(1,num):
    print("*"*(num+4))

//11th pattern
num=10
print(" "*num+"*"*(num+6))
for i in range(1,num):
    print(" "*(num-i)+"*"+" "*(num+4)+"*")
print("*"*(num+6))
    
