
# # Que.8

# Write a program to find out whether a file 
# is identical and matches the content of another file.

with open("This text.txt")as f:
    content1 = f.read()

with open("This_Copy.txt")as f:
    content2 = f.read()

if (content1 == content2):
    print("This file are identical.")

else:
    print("No this file are not identical.")

