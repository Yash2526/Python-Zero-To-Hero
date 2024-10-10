

# Que.5

# Write a program to mine a log file and find out whether it contains Python word. 

with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes! It is present.")

else:
    print("No It is not present.")

