def increment(no):
    try:
        return int(no) + 1
    except:
        raise ValueError("This is not working")

a=increment(7)
print(a)