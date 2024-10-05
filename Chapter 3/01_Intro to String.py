# Ch.3 = Strings

# Strings are mainly 3 types

# a = 'Harry'        # Single quoted string
# b = "Harry"        # Double quoted string
# c = '''Harry'''    # Triple quoted string

# Positive Slicing - 

# Name =  "H  a  r  r  y"    One type of string.
         # 0  1  2  3  4    - Positive Slicing.
         # -5 -4 -3 -2 -1     -Negative Slicing.



# POSITIVE SLICING #

name = "harry"

nameshort = name[0:4]       # That means it will start to print from 0 - 3

print(nameshort)

character1 = name [1]   # That means it will print the 1st character of Harry word.

print(character1)


# # NEGATIVE SLICING #

# Note. Whenevr you have to do negative slicing at that,
#         time the easy way to do it by doing the corresponding positive slicing number.


# SLICING WITH THE SKIP VALUE

word = "amazing"

print(word[1:6:2]) # It will print basically ''mzn'


yash = "abcdefghijklmnopqrstuvwxyz"

print(yash[0:9:2])



print(len(name)) # it will Give you the length of character.

print(name.endswith("rry")) # That simply means it will tell you the word which is ends with the letter 'rry',
                                # is actually exist or not and if exist it will print true.


print(name.startswith("Ha"))

print(name.capitalize())    # it will basically capitalize the 1st letter of word.

