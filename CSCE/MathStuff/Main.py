from decimal import InvalidOperation
from Math_Stuff import Math_Stuff_Class

option = -1
while option != 4:
    option = int(input("Please Enter an Option\n1. Find the Median\n2. Find the Square\n3.Find The Times Table\n4. Quit\n"))

    if option == 1:
        medList = []
        for x in range (0, 10):
            medList.append(int(input("Enter Number "+str(x+1)+":\t")))
        ret = Math_Stuff_Class.Median(medList)
        print("The Median is: "+str(ret))
    elif option == 2:
        squaredList = []
        for x in range (0, 10):
            squaredList.append(int(input("Enter Number "+str(x+1)+":\t")))
        Squareret = Math_Stuff_Class.Square(squaredList)
        print(Squareret)
    elif(option == 3):
        num = int(input("Enter a number:\t"))
        Math_Stuff_Class.Times_Table(num)