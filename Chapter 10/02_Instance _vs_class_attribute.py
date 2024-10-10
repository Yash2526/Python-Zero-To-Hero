

class Student:
    name = "Yash"  # Class attribute
    Rollnumber = 25
    sub = "English"

# Note - Instance attribute take prefernce over class attribute

kalyani = Student()
kalyani.name = "Kalyani"  # Instance attribute

print(kalyani.name, kalyani.sub)

