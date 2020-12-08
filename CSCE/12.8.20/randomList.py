import random
import statistics

numlist = []
randInt = random.randint(0, 10)
for i in range(randInt):
    addIn = int(input("Enter a Number:\t"))
    numlist.append(addIn)

option = int(input("\n1. Sum of List\n2. Mean of List\n3, Sorted List\n"))
if option == 1:
    answer = sum(numlist)
    print("The Sum is " + str(answer))

elif option == 2:
    answer = statistics.mean(numlist)
    print("The Mean is " + str(answer))

elif option == 3:
    numlist.sort()
    print(numlist)
