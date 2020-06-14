
# Over Under Game
def overUnder():

    import random
    trigger = "yes"
    while(trigger.lower() == "yes"):
        num1 = random.randint(0,100)
        overUnderGuess = raw_input("The Number is {0}. Will the next number be over or under?\n".format(num1))
        if(overUnderGuess.lower() != "over" and overUnderGuess.lower() != "under"):
            print("Invalid Input")
            break
        num2 = random.randint(0,100)
        if(num1 > num2):
            if(overUnderGuess.lower() == "over"):
                print("Sorry the number was {0}").format(num2)
            elif(overUnderGuess.lower() == "under"):
                print("Congrats the number was {0} you won!").format(num2)
        elif(num2 > num1):
            if(overUnderGuess.lower() == "over"):
                print("Congrats the number was {0} you won!").format(num2)
            elif(overUnderGuess.lower() == "under"):
                print("Sorry the number was {0}").format(num2)
        else:
            print("Whoops! It was the same!")
        trigger = raw_input("Would you like to play again\n")

#Math Problem Simulator
def mathGame():
    import random
    usanswer = 0
    while(usanswer != 404):
        print("Type 404 to quit")
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        symb = random.randint(0,2)
        symbols = ["*", "+", "-"]

        if symb == 0:
            answer = num1*num2
        elif symb == 1:
            answer = num1+num2
        elif symb == 2:
            answer = num1-num2

        symbtext = symbols[symb]
        usanswer = input("What is {0}{1}{2}?\t".format(num1, symbtext, num2))

        if(answer == usanswer):
            print("You are correct!\n")
        if(usanswer == 404):
            print("Goodbye!")
        else:
            print("You are wrong!\n")


def changeMaker():
    c = input("How much is owed to the user?\t$")
    c = c*100 #Formating to Maker it Look nicer, not needed though
    print(int(c//2000), "twenty")
    c = c%2000
    print(int(c//1000), "tens")
    c = c%1000
    print(int(c//500), "fives")
    c = c%500
    print(int(c//100), "dollars")
    c = c%100
    print(int(c//25), "quarters")
    c = c%25
    print(int(c//10), "dimes")
    c = c%10
    print(int(c//5), "nickles")
    c = c%5
    print(int(c//1), "pennies")
    


#Tester

overUnder()
mathGame()
changeMaker()
