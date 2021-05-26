num=int(input("Enter any number to see the table of that number: "))
table=[num*i for i in range(1,11)]
print(table)
with open("table.txt","a") as f:
    f.write(str(table)) 
    f.write("\n")