while(True):
    a=input("Enter the no.  :")
    print("press t to terminate")
    if a=='t':
        break
    try:
        a=int(a)
        if a>10:
            print("you entered the larger value")
    except Exception as e:
        print(e)
print("thanks for playing")

