
class Student:
    name = "Yash"       # Class attribute
    Rollnumber = 25
    sub = "English"


    def __init__(self,name,language,salary):  # This is dounder method which is automatically called.
        self.name = name
        self.language = language
        self.salary = salary

        print("I am creating an object.")
        

kalyani = Student("Harry","JavaScript",100000)

kalyani.name = "Kalyani"     # Instance attribute

print(kalyani.Rollnumber,kalyani.name, kalyani.sub,kalyani.language,kalyani.salary)

# rohan = Student()
