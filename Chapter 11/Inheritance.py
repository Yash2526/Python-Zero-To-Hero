
# Types of inheritance 
        # 1. Single Inheritance


class Employee:     # Parent Class
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class Programmer:     #  Child Class
    Company = "ITC Infotech"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language.")



class Programmer(Employee): # This is nothing but the Single Inheritance.
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")




a = Employee()
b = Programmer()

print(a.company,b.company)
