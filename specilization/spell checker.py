import re

## finding the unique words
# fd=open("big.txt","r")
with open("big.txt","r") as fd:
    lines=fd.readlines()
    words=[]
    for line in lines:
        words+=re.findall("\w+",line.lower())
print(len(words))
vocab=list(set(words))
print(len(vocab))

## finding the probablity distribution
word_probability={}
for word in vocab:
    word_probability[word]=float(words.count(word)/len(words))
    
print(word_probability)
print(words.count("future"))
