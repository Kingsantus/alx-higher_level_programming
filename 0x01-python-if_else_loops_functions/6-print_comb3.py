#!/usr/bin/python3
for i in range(9):
    for a in range(10):
        if i != a and i < a:
            if i == 8 and a == 9:
                print("{}{}".format(i, a), end='\n')
            else:
                print("{}{}".format(i, a), end=', ')
