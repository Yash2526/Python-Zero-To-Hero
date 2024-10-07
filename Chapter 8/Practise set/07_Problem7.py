
# Que.7

# Write a python function to remove a given word from a list and ad strip
# it at the same time.

def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
       

l = ["Harry","Yash","Rohan","Kalyan","Sonu","an"]

print(rem(l,"an"))