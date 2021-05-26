list1=[34,56,56,2,6,7,8,59]
''' list2=[] # to store even no.
    for items in list1:
        if items>=8:
            list2.append(items) '''
# another way to do same thing
list2=[i for i in list1 if i>=8] #comprehension is nothing but to create list from existing list
print(list2)

# to do same thing to print a set
set={i for i in list2 if i%2==0}
print(set)