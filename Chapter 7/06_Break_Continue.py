


for i in range(100):
    if(i==33):
        break        # the function of break is too exit the loop right now.
    print(i)


for i in range(100):
    if(i==33):
        continue       # The function of continue is to skip the perticular iteration.
    print(i)           # it simplly means it will skip 34 and remaining will print.


for i in range(0,80):
    print(i)
    if (i==3):
        break

    for i in range(4):
        print('printing')
        if(i==2):
            continue
        print(i)