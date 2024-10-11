
# Que.2

# Create a class Pets from a class Animal and further create a class Dog from pets
# add a method bark to class Dog


class Animal:
    pass
   
class Pets(Animal):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow !")

d = Dog
d.bark()

