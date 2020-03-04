import random

def string_maker():
    s = ''
    list = '.1234.....56789'
    for i in range(81):
        s += random.choice(list)

    return s

print(string_maker())
