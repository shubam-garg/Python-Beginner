''' create a class pets from class animals and further create class dog from pets,
    add a method bark to class dog '''
class animals:
    animaltype="Mammal"

class pets(animals):
    petcolor="Black"

class dog(pets):
    
    @staticmethod
    def bark():
        print("dog")

d=dog()
d.bark()