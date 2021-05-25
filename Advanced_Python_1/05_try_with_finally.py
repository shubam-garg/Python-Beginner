try:
    no=int(input("Enter the number : "))
    a=70/no
    print(a)
except Exception as err:
    print(err)
    exit()
finally:
    print("It will work in every situation")

print("It will not print because exception given the command exit(),it will run only if try exiqute")