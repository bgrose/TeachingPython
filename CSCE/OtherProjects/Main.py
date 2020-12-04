from Clothes import Shirt
from Clothes import Pants
from Clothes import Other


Catalog = []
option = 0

while option != 5:
    option = int(input("Enter Number For Menu\n1. Add Shirt\n2. Add Pants\n3.Add Other\n4.Print Catalog\n5.Exit\n"))
    if(option == 1):
        temp = Shirt()
        Catalog.append(temp)
    elif(option == 2):
        temp = Pants()
        print(temp)
        Catalog.append(temp)
    elif(option == 3):
        temp = Other()
        Catalog.append(temp)
    elif(option == 4):
        print("\nCATALOG")
        for obj in Catalog:
            print(obj)
    elif(option!=5):
        print('INVALID SELECTION\n')

