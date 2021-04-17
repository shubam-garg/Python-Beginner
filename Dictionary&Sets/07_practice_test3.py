# 3) can we have a set of 18 (int) and "18"(str) as a values in it.
ws = {18,"18",18.8}
print(ws)

''' 4) What will be the length of the followinf set s
    s=set()
    s.add(20)
    s.add(20.0)
    s.add("20") '''
s=set()
s.add(20)
s.add(20.0)  # either this no is float but it's value is equal to integer 20
s.add("20")
print(s)
print(len(s))

# 5) r={} what will be the type of set
r={}
print(type(r)) # dict