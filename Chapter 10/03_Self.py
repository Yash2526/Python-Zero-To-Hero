
class Employee:
    language = "Python"   # Class attribute
    salary = 50000
    name = "Yash"

# Note-def getInfo this is method in this method "self" is imp to give in every time. 

    def getInfo(self): 
        print(f"The language is {self.language} & your salary is {self.salary}")
        
    
    def greet(self):
        print(f"Good Morning! {self.name}")

# if we don't want to pass the self object then we can give the '@staticmethod'

    @staticmethod   
    def x():
        print("Hello")

harry = Employee()
harry.language = "JavaScript"   # This is a instance attribute.

harry.x()             # In the following 2 ways we can getInfo
harry.greet()             # In the following 2 ways we can getInfo
Employee.getInfo(harry)