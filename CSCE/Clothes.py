class Shirt:
    def __init__(self):
        self.size = input("Enter the shirt size:    ")
        self.color = input("Enter the shirts color:    ") 
        self.name = input("Enter the Shirt name:    ")
    def __str__(self):
        ret = "SHIRT\nSize: {}\nColor: {}\nName: {}\n".format(self.size, self.color, self.name)
        return ret
class Pants:
    def __init__(self):
        self.waist = input("Enter the pants waist:    ")
        self.length = input("Enter the pants length:    ") 
        self.name = input("Enter the pants name:    ")
    def __str__(self):
        ret = "PANTS\nWaist: {}\nLength: {}\nName: {}\n".format(self.waist, self.length, self.name)
        return ret
class Other:
     def __init__(self):
        self.color = input("Enter the others color:    ") 
        self.name = input("Enter the others name:    ")
     def __str__(self):
        ret = "OTHER\nColor: {}\nName: {} \n".format(self.color, self.name)
        return ret
