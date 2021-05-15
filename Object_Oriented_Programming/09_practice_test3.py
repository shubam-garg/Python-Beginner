# Create a class with class attribute a; create any object from it and set a directly using object.a=0.
# Does this change the class attribute.

class attribute:
    a = 10
   
obj = attribute()
obj.a = 0
print(attribute.a)
print(obj.a)
    