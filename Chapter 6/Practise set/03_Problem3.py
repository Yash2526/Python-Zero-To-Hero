
# Que.3

# A span comment is defined as a text containing following keywords

s1 = "Make a lot of money"
s2 = "Buy now"
s3 = "Click this"
s4 = "Subscibe this"

# Write a program to detect this spam

message = input("Enter your comment: ")

if((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message)):
    print("This is a spam message")

else:
    print("This is not a spam message")
