print(ord("A"))
name= "Monika Chauahn"

for i in name:
    print(ord(i))
    
print([i for i in name])  
print([ord(i) for i in name])     

## print A -Z
print("".join([chr(i) for i in range(65,91)]))

## print Z_A
print("".join([chr(i) for i in range(91,65,-1)]))

## print a-z
print("".join([chr(i) for i in range(97,123)]))

## print z-a
print("".join([chr(i) for i in range(123,97,-1)]))

## pattern
for i in range(65,97):
    for j in range(65,97):
        print(chr(i)+chr(j))


## DIY function capitalize
text="hello"
def capital_(text):
    if (len(text)!=0):
        return text[0].upper() + text[1:].
lower()
    else:
        return None
print(capital_("hello baby. How are you"))

# upper case
tt="HEllo Guys"

def upper(text):
    result=""
    for char in text:
        if (ord(char)>=97 and ord(char)<=123):
            result+=chr(ord(char)-32)
        else:
            result+=char
    return result
upper(tt)
print(tt.upper())

# lower case
tt="HEllo Guys"

def lower(text):
    result=""
    for char in text:
        if (ord(char)>=66 and ord(char)<=96):
            result+=chr(ord(char)+32)
        else:
            result+=char
    return result
lower(tt)
print(tt.lower())


#isaplha 
def isalpha(text):
    c=0
    for i in text:
        if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=66 and ord(i)<=97):
            c+=1
    if (len(text)==c):
        return True
    else:
        return False
print(isalpha("monikaChauhan"))
print("monikachauhan".isalpha())

#isdidgit
def isdigit(text):
    c=0
    for i in text:
        if (ord(i)>=48 and ord(i)<=57):
            c+=1
    if (len(text)==c):
        return True
    else:
        return False
print(isdigit("123/4"))
print("23/45".isdigit())

#isalnum
def isalnum(text):
    c=0
    for i in text:
        if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=66 and ord(i)<=97) or (ord(i)>=48 and ord(i)<=57):
            c+=1
    if (len(text)==c):
        return True
    else:
        return False
print(isalnum("monikaChauhan43"))
print("monikachauhan2".isalnum())


## title
def title(text):
    output=[]
    for char in text.split(" "):
        output.append(upper(char[0])+lower(char[1:]))
    return " ".join(output)
print("monika chauahn".title())
print(title("monika chauhan"))
        