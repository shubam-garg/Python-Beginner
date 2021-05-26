# write a program to print 3,5,7 element from a list using enumerate function
list=[35,57,378,590,97,53,7,24,56]
for index,item in enumerate(list):
    if index==2 or index==4 or index==6:
        print(index,item)
    