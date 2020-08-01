from matplotlib import pyplot as plt

#Lists for Variables of Data
nameData = []
catagoryData = []
priceData = []

def BarGraph(xAxisData, yAxisData, xAxisLabel, yAxisLabel, title):
    plt.bar(xAxisData, yAxisData)
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.title(title)
    plt.show()
    

def LineGraph(xAxisData, yAxisData, xAxisLabel, yAxisLabel, title):
    plt.plot(xAxisData, yAxisData)
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.title(title)
    plt.show()

def SaveGraph(xAxisData, yAxisData, xAxisLabel, yAxisLabel, title):
    plt.bar(xAxisData, yAxisData)
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.title(title)
    plt.savefig('graph.png')

def addData(name, catagory, price):
    if not nameData:
        nameData.insert(0, name)
        catagoryData.insert(0, catagory)
        priceData.insert(0, price)
    else:
        nameData.append(name)
        catagoryData.append(catagory)
        priceData.append(price)
    print("Data has been added")

def menu():
    option = int(input("\n1. Log a new item\n2. Create a bar graph of existing data\n3. Create a line graph of the existing data\n4. Save the existing data graph\n5. Exit\n"))
   
    #Log a New Item
    if(option == 1):
        name = raw_input("What is the Name of the Collectable: ")
        catagory = raw_input("What is the Catagory of the Collectable: ")
        price = float(input("What is the Price of the Collectable: "))
        addData(name, catagory, price)

        #Loops back to menu
        menu()

    #Bar Graph
    elif(option == 2):
        graphMethod = int(input("Would you like to graph the data based on\n1. Price\n2. Catagory\n"))
        if(graphMethod == 1):
            BarGraph(nameData, priceData, "Name", "Price", "Price vs Name Graph")
        elif(graphMethod  == 2):
            BarGraph(nameData, catagoryData, "Name", "Catagory", "Catagory vs Name Graph")
        #Loops back to menu
        menu()

    #Line Graph
    elif(option == 3):
        graphMethod =  int(input("Would you like to graph the data based on\n1. Price\n2. Catagory\n"))
        if(graphMethod == 1):
            LineGraph(nameData, priceData, "Name", "Price", "Price vs Name Graph")
        elif(graphMethod  == 2):
            LineGraph(nameData, catagoryData, "Name", "Catagory", "Catagory vs Name Graph")
    
        #Loops back to menu
        menu()

    #Save Graph
    elif(option == 4):
        graphMethod =  int(input("Would you ike to graph the data based on\n1. Price\n2. Catagory\n"))
        if(graphMethod == 1):
            SaveGraph(nameData, priceData, "Name", "Price", "Price vs Name Graph")
        elif(graphMethod  == 2): 
            SaveGraph(nameData, catagoryData, "Name", "Catagory", "Catagory vs Name Graph")
        #Loops back to menu
        menu()
    elif(option == 5):
        exit
    else:
        print("Not a Valid Option\n")
        
        #Loops back to menu
        menu()

#Runner
menu()