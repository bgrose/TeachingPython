import random

num =  random.randint(1, 200)
for i in range(10):
    user = int(input("Enter Your Guess: "))
    if(num > user):
        print("\nToo Low. Try Again")
    elif(num < user):
         print("\nToo High. Try Again")
    else:
        if(i < 5):
            print("Great Job!")
            break
        else:
            print("You win!")
            break

    if(i == 9):
        print("You Lose")