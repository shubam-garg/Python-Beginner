class bone:
    size=23
    place="leg"
    def chgsize(self,s,p):
        self.size=s
        self.__class__.place=p # THE value of attribute of class will change, another way to do same thing

    ''' @classmethod
        def chgplace(cls,p):
            cls.place=p      '''

b=bone()
print(b.size)
print(b.place)
b.chgsize(34,"mouth")
print(b.size)
print(b.place)
print(bone.size)
print(bone.place)
