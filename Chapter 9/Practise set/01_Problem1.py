
# Que.1

# Write a program to read the text from a given file'poems.txt'and find out 
# whether it contains the word twinkle.

f = open("poems.txt")

content = f.read()

if("Twinkle" in content):
    print("The Word Twinkle is present in the content.")

else:
    print("The Word Twinkle is not present in the content.")

f.close()
