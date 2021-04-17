''' 6) Create an empty Dictionary. Allow 4 friends to enter their 
    favourite language as a value and their name as a key.
    Assume the names are unique. '''
a=input("Enter 1 your name\n:")
b=input("Enter 2 your name\n:")
c=input("Enter 3 your name\n:")
d=input("Enter 4 your name\n:")
e=input("Enter 1 country name\n:")
f=input("Enter 2 country name\n:")
g=input("Enter 3 country name\n:")
h=input("Enter 4 country name\n:")
dic={}
dic[a]=e
dic[b]=f
dic[c]=g
dic[d]=h
print(dic)

''' 7) In same program if name of 2 friends will be same,
    what will be the problem. '''

dic[a]=e
dic[b]=f
dic[a]=g
dic[d]=h
print(dic)# key value will update

''' 8) In same program if country is same of 2 friends will be same,
    what will be the problem. '''

dic[a]=e
dic[b]=e
dic[c]=g
dic[d]=h
print(dic)# value can be same

''' can you change the value of list which contain in the list s, s={8,7,12,shubam,[1,2]}
    it is theory question.
    Ans is no because list is part of set and set is hashable in which no value can be change. '''