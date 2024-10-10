
# Que.6

# Write a program to find out the line number where the python is present from Q.5


with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes it is present. line no: {lineno}")
        break
    lineno += 1

else:
    print("No It is not present.")





