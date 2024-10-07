
# Que.2

# Write a program to greet all the persons names stored in
# a list 'l' and which start with 's'

l = ["Harry","Soham","Sachin","Rahul","Sonali"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
        