
# Que.4

# A file contains a word "Donkey" multiple times you need to write 
# program which replace this words with ##### by updating the same file.



word = "Donkey"

with open("D.txt","r") as f:
    content = f.read()

newcontent = content.replace(word, "#####")

with open("D.txt",'w') as f:
    content = f.write(newcontent)




# Que.5

# Repeat program 4 for a list of word to be censored.

words = ["Harry","Lion","Monkey","Tiger"]

with open("D.txt")as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#"*len(word))


with open("D.txt","w")as f:
    f.write(content )



