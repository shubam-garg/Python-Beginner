try:
    no=int(input("enter the number: "))
    a=47/no
    print(a)
except Exception as e:
    print(e)
else:
    print("There is no problem in try,it works...")