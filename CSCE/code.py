class myClass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getSum(self):
        return self.x+self.y

obj= myClass(3,4)
print("Sum =",obj.getSum())