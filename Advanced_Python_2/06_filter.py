list1=[4,2,1,3,7]
def less_than_5(num):
    if num<5:
        return True
    else:
        return False

print(list(filter(less_than_5,list1 )))