#write a class complex to represent complex numbers,along with overload operators + and *.

class complex:
    def __init__(self,real,imaginary):
        self.num1=real
        self.num2=imaginary

    def __add__(self,c):
        return complex(self.num1+c.num1,self.num2+c.num2)

    def __mul__(self,c):
        mulreal=self.num1*c.num1-self.num2*c.num2 #(a+bi)(c+di)=(ac-bd)+(ad+bc)i
        mulimg=self.num1*c.num2+self.num2*c.num1
        return complex(mulreal,mulimg)

    def __str__(self):
        return f"{self.num1}+{self.num2}i"


c1=complex(20,4)
c2=complex(10,6)
print(c1+c2)
print(c1*c2)