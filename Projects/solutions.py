
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


    


#Debug Tester (Change Out Exercise Number)
def main():
    overUnder()
if __name__ == "__main__":
    main()

