def Fahrenheit_to_Celsius(num):
    ret = (num - 32) * (5/9)
    return ret
def Celsius_to_Fahrenheit(num):
    ret = (num * 9/5) +32
    return ret
def Feet_to_Meters(num):
    ret = num / 3.281
    return ret
def Meter_to_Feet(num):
    ret = num * 3.281
    return ret
def Feet_to_Miles(num):
    ret = num / 5280
    return ret
def Miles_to_Feet(num):
    ret = num * 5280
    return ret
def Meters_to_Miles(num):
    ret = num / 1609
    return ret
def Miles_to_Meters(num):
    ret = num * 1609
    return ret
def Pounds_to_Kilograms(num):
    ret = num / 2.205
    return ret
def Kilograms_to_Pounds(num):
    ret = num * 2.205
    return ret


option = -1
while(option != 4):
    option = int(input("1. Tempature\n2. Length\n3.Weight\n4. Quit\n"))
    if(option == 1):
        tempOp = int(input("1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n"))
        if(tempOp == 1):
            num = int(input("Enter the Number:\t"))
            print(str(Fahrenheit_to_Celsius(num)) + " Celcius")
        elif(tempOp == 2):
            num = int(input("Enter the Number:\t"))
            print(str(Celsius_to_Fahrenheit(num)) + " Fahrenheit")
    elif(option == 2):
        lengthOp = int(input("1. Feet to Meters\n2. Meters to Feet\n3. Feet to Miles\n4. Miles to Feet\n5. Meters to Miles\n6. Miles to Meters\n"))
        if(lengthOp == 1):
            num = int(input("Enter the Number:\t"))
            print(str(Feet_to_Meters(num)) + " Meters")
        elif(lengthOp == 2):   
            num = int(input("Enter the Number:\t"))
            print(str(Meter_to_Feet(num)) + " Feet")
        elif(lengthOp == 3):
            num = int(input("Enter the Number:\t"))
            print(str(Feet_to_Miles(num)) + " Miles")
        elif(lengthOp == 4):
            num = int(input("Enter the Number:\t"))
            print(str(Miles_to_Feet(num)) + " Feet")
        elif(lengthOp == 5):
            num = int(input("Enter the Number:\t"))
            print(str(Meters_to_Miles(num)) + " Miles")
        elif(lengthOp == 6):
            num = int(input("Enter the Number:\t"))
            print(str(Miles_to_Meters(num)) + " Meters")
    elif(option == 3):
        weightOp = int(input("1. Pounds to Kilograms\n2. Kilograms to Pounds\n"))
        if(weightOp == 1):
            num = int(input("Enter the Number:\t"))
            print(str(Pounds_to_Kilograms(num)) + " Kilograms")
        elif(weightOp == 2):
            num = int(input("Enter the Number:\t"))
            print(str(Kilograms_to_Pounds(num)) + " Pounds")