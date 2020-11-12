
class DataThing:

    def __init__(self, _x):
        self.y = int(input("Enter a Y Value:    "))
        self.x = _x
    def __str__(self):
        ret = "{} {}".format(self.x, self.y)
        return ret

def createSome():
        x = int(input("Enter a X Value:    "))
        ret = DataThing(x)
        return ret
        


########### Tester ###############

a = DataThing(5)
print(a)
b = createSome()
print(b)