

class Employee :   
    language = "py"     # This is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry"
print(harry.name, harry.salary, harry.language)


kalyani = Employee()
kalyani.name = "Kalyani"   # This is a instance attribute
print(kalyani.name, kalyani.language, kalyani.salary)


# Here name is object Attribute and salary and language are class attribute as 
# they directly belong to the class.





