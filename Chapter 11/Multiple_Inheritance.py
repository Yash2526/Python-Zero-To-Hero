
# 2. Multiple Inheritance

class Employee:
    company = "ITC"
    name = "Yash"
    salary = 500000

    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class Coder:
    language = "Python"
    def printlanguages(self):
        print(f"This is my fev language {self.language}")


class programmer(Employee,Coder):   # Here we mearge the both clss and created  a new one wich have data of both the classes.
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"My name is {self.name} and i am good with {self.language} language.")

a = Employee()
b = programmer()

b.show()
b.printlanguages()
b.showlanguage()

print(a.name,a.company,a.salary)




