
# Que.7

# Write a program to make a copy of a text file "This text"

with open("This text.txt")as f:
    content = f.read()

with open("This_Copy.txt","w")as f:
    f.write(content)

    