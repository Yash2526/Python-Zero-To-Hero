

# Que.5

''' Create an empty dict allow 4 friends to enter thier favourite 
language as a value and use key as their names,assume that the names are unique.'''


friends = {}

f1 = input("Enter your name: ")
lan = input("Enter your regional language: ")
friends.update({f1:lan})

f2 = input("Enter your name: ")
lan = input("Enter your regional language: ")
friends.update({f2:lan})

f3 = input("Enter your name: ")
lan = input("Enter your regional language: ")
friends.update({f3:lan})

f4 = input("Enter your name: ")
lan = input("Enter your regional language: ")
friends.update({f4:lan})

print(friends)
