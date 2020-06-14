# Example 1
def exercise1():
    print("Hello World")

# Example 2
def exercise2(x,y):
    print(x+y)
    print(x*y)

# Example 3
def exercise3(n):
    sum = 0
    for curr in range(1, n + 1):
       sum = sum + curr
    print(sum)

# Example 4
def exercise4(miles):
    feet = miles*5280
    print('There are {0} feet in {1} miles.').format(feet, miles)

# Example 5
def exercise5(age):
    if age < 7:
        print('Have a glass of water.')
    elif age < 21:
        print('Have a Coke.')
    else:
        print('Have some Sangria.')

# Example 6
list = ['Keanu', 'River', 'Leonardo', 'Brad', 'A', '1998']

def exercise6():
    print(list)
    print(list[0])
    print(list[-1])
    print(list[3:5])
    print(list[:3])
    print(list[3:])
    print(len(list))
    list.append('z')
    print(list)

# Example 7
def exercise7():
    print("\n")
    b1 = int(input ("\nWhat is the bottom base\t\t"))
    b2 = int(input ("\nWhat is the top base\t\t"))
    h = int(input ("\nWhat is the height\t\t"))
    area = (0.5)*((b1+b2)*h)
    print("The area of a trapezoid with bases {0} and {1} and height {2} is {3}").format(b1, b2, h, area)

# Example 8
def exercise8(mon, day, year):
    months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    print(str(months[mon]) + '/' + str(day) + '/'+ str(year))

# Example 9
def exercise9(ele):
    import csv

    f = open("Introduction\periodictable.csv")
    dict = {}

    for row in csv.reader(f):
       dict[row[2]] = row[0], row[1]

    if ele.lower():
        cap = ele.capitalize()
        print(dict[cap])
    else:
      print(dict[ele])

    f.close()

#Tester
exercise1()
exercise2(2, 5)
exercise3(22)
exercise4(5)
exercise5(22)
exercise6()
exercise7()
exercise8("June", 24, 1998)
exercise9("Gold")
