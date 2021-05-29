list1=[2,5,8,58,46]
def func(num):
    return num*num
'''
Method 1
a=[]
for item in list:
    a.append(func(item))
print(a) '''
# another method to do same thing
"Method 2"
print(list(map(func,list1)))