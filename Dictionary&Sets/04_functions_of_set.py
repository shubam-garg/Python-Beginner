z= set ()
print(type(z))
# for a adding values in an empty set
z.add(1)
z.add(5)
z.add(5)
# z.add([90,4,6]) # can not add list in set because list can be change / not hashble
# z.add({4:15,6}) # can not add dictionary in set because dictionary can be change / not hashble
z.add((23,22,45)) # tuple will add in set
print(z)

# to find the length of set
print(len(z))

# to remove any particular element or tuple from set
z.remove((23,22,45))
print(z)
z.remove(1)
print(z)
z.add(34)
z.add(3)
z.add(4)

# to remove arbitrary(any) element from set pop function is used
print(z)
print(z.pop()) # return the removed element
print(z)

# clear method to clear all the elements from the set
print(z.clear()) # return none
print(z) # set is empty (output: "set()" )

# union and intersection method
r1={2,5,8,3,9}
r2={2,9}
r3={9,4,1,2,7}
print(r1^r3) #intersection
print(r1-r3)
print(r3-r1)