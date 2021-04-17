''' 2)Write a program to input 8 numbers from user 
    and display all the unique numbers once '''
z=set()
a=int(input("Enter 1 no.\n:"))
b=int(input("Enter 2 no.\n:"))
c=int(input("Enter 3 no.\n:"))
d=int(input("Enter 4 no.\n:"))
e=int(input("Enter 5 no.\n:"))
f=int(input("Enter 6 no.\n:"))
g=int(input("Enter 7 no.\n:"))
h=int(input("Enter 8 no.\n:"))
z.add(a)
z.add(b)
z.add(c)
z.add(d)
z.add(e)
z.add(f)
z.add(g)
z.add(h)
print(z)
# or direct method
z={a,b,c,d,e,f,g,h}
print(z)