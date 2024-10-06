

marks = {
    #This are all items
    "Harry":100,
    "Yash":99,
    "Rohan":85,
    "Mahesh":75,
    0:"Sahil"

}

# Methods of dictionary

print(marks.items())     # It gives the all items of key value pair in the Dictionary.

print(marks.keys())       # It gives you keys("Harry,Yash etc...")

print(marks.values())       # It gives you values ("100,99,85, etc..")

marks.update({0:"Athrva","Sahil":60}) # it will do changes if key value is exiest already else it will add it.


print(marks.get("Harry"))
print(marks["Harry"])


print(marks.get("Harry2"))       # It will print None.
print(marks["Harry2"])           # Returns an Error.


print(marks)  