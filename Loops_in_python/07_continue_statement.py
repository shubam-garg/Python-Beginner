for i in range(6):
    if(i==2): # loop will continue but 2 will not execute  
        continue
    print(i)

for k in range(6):
    if(k<=2): # loop will continue but values less than 0r equal to 2 will not execute  
        continue
    print(k)
# print("In continue statement the values come under if loop will not execute")

# if want to print even no
for l in range(0,10):
    if(l%2!=0):
        continue
    print(l)