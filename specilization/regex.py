import re

# ## serach 
print(re.search("what","what is you name"))

txt="Hello guys hope You all are doing well,you just tell me"
print(re.search("you",txt.lower()))


## find all 
print(re.findall("you",txt.lower()))

## finditer
for i in re.finditer("is","this is a good boy. he is not bad"):
    print(i.span())
    
    
## creating regular expression
txt="My phone number is 88-6254-6254"
pattern="\d\d-\d\d\d\d-\d\d\d\d"
print(re.findall(pattern,txt))

pattern="\d{2}-\d{4}-\d{4}"
print(re.findall(pattern,txt))

pattern="\w\w\w"
print(re.findall(pattern,txt))

##simple serach
txt="The Man call the van to make a gang with tan people"
print(re.findall("an",txt))

## strating of search with specific text
txt="The Man call the van to make a gang with tan people"
print(re.findall(".an",txt))

## endingof search with specific text
txt="The Man call the van to make a gang with tan people"
print(re.findall("t.",txt))

## upper word
txt="The Man call the van to make a gang with tan people"
print(re.findall("[A-Z]",txt))

## lower word
txt="The Man call the van"
print(re.findall("[a-z]",txt))

## numbers
txt="The Man call the van number 1234"
print(re.findall("[0-9]",txt))

## starting and end pattern matching
s="this 5 is not divisible by 6 and 9"
print(re.findall("\d",s))

s="This 5 is not divisible by 6 and 9"
print(re.findall("\d$",s))

s="5 is not divisible by 6 and 9"
print(re.findall("^\d",s))

##upper case lower case and numerbs
txt="This 5 is not divisible by 6 and 9"
print(re.findall("[A-Za-z0-9]",txt))


