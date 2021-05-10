# f = open("rendom1.txt", "w") # want to completely new
f = open("rendom1.txt", "a")# to add data in existing file
out = f.write('''
Upload in file''')# how many times u run it, it will go to file
print(out)
f.close()