
# Que.2

# Write a program to fill in a letter template given below with name and date.

letter = ''' Dear <|Name|>,
You are selected!
<|Date|>'''

print("Congratulations ")

print(letter.replace("<|Name|>" ,"Yash").replace("<|Date|>", "25 march 2025"))