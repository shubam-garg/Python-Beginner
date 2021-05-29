from functools import reduce
list1=[43, 9, 5, 34]

sum = lambda x, y: x+y
print(reduce(sum,list1)) 
''' it work like
    x=43,y=9: 43+9=52
    x=52,y=5: 52+5=57
    x=57,y=34: 57+34=91 '''