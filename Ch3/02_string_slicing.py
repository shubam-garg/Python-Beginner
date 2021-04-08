# concatenating: bring two strings togeather
Name = "rony"
greeting = 'good morning'
#c = greeting + Name
#print(c)
#print(Name[0])
print(Name[0:4])# : for giving starting and ending position of index of srting
#length of string from 0 to -1 from given last array position
#print(Name[:4]) # is same as Name[0:4] automatically
print(greeting[0:]) # is as same as greeting[0:13] automatically

# negative indices : 
# it can aslo be used as shown in the figure below -1 corresponds to the (length -1) index,-2 to(length-2).
'''     r     o     n     y
        [0]   [1]   [2]   [3]
        [-4]  [-3]  [-2]  [-1]  '''
f=greeting[-5:-1] # is as same as greeting[0:13] automatically
print(f)

# slicing with skip value
g = "garg@@raikot"
print(g[0:13:2]) # third digit in breaket stands for skip index values after one letter every time
print(g[0::3]) # third digit in breaket stands for skip index values after two letter every time
