# create class c-2d vector and use it to create another class reprsenting a c-3d vector.

class c2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"

class c3dvec(c2dvec):
    def __init__(self, i,j,k):
        super().__init__(i, j)
        self.kcap=k

    def __str__(self):
        return super().__str__()+f"+{self.kcap}k"

c2=(5,7)
c3=c3dvec(3,5,9)
print(c2)
print(c3)
