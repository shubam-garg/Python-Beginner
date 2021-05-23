class vector:
    def __init__(self, vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1 +=f"{i}=i[{index}] "
            index +=1
        return str1

    def __add__(self,vec2nd):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2nd.vec[i])
        return vector(newlist)
    
    def __mul__(self,vec2nd):
        sum=0
        for i in range(len(self.vec)):
            sum +=(self.vec[i]*vec2nd.vec[i])
        return sum

    def __len__(self):
        return len(self.vec)

v1=vector([1,4,5])
v2=vector([7,2,7])
print(len(v1))
print(len(v2))