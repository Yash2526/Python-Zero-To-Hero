
# enumerate function

l = [125,500,158,956,1000,789]

# index = 0
# for item in l:
#     print(f"The items number at index {index} is {item}")
#     index += 1


# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The items number at index {index} is {item}")

