def divby4(x, y):
    ret = []
    for i in range(x, y+1):
        if (i % 4 == 0):
            ret.append(i)
    return ret

ret = []
ret = divby4(4, 100)
print(ret)