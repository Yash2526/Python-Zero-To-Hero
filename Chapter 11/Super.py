
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1


class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    
    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()      # Super is use to To Run the Constructor call of parent class.
        print("Constructor of Manager")
    c = 3


# o = Employee()
# print(o.a)  # Prints the a attributes.
# # print(o.b)  # Shows an error as there is no b attribute in employee class.

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a,o.b,o.c)

