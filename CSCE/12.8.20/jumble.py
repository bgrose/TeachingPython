import random

def Jumble(_list):
    swaps = int(input('How Many Swaps to Make: '))
    for i in range(swaps):
        randint1 = random.randint(0, len(_list)-1)
        randint2 = random.randint(0, len(_list)-1)
        temp = _list[randint1]
        _list[randint1] = _list[randint2]
        _list[randint2] = temp
        return _list

l = [1,2,3,4]
new_l = Jumble(l)
print(new_l)