list=[34,56,323,4.6,True,"Parmish"]
''' index=0
    for items in list:
        print(items)
        index += 1  '''
# easy way to do same thing
for index,item in enumerate(list): # in this python give priority to item,index
    print(item,index)              # in this python give priority to item,index.........