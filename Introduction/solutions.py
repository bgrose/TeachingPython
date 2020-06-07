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
def exercise7(file, ele):
    import csv
    
    f = open(file)
    dict = {}
    
    for row in csv.reader(f):
        dict[row[2]] = row[0], row[1]
    
    if ele.lower():
        cap = ele.capitalize()
        print(dict[cap])
    else:
        print(dict[ele])
        
    f.close()

# Example 8
def exercise8(mon, day, year):
    months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    print(str(months[mon]) + '/' + str(day) + '/'+ str(year))


#Debug Tester (Change Out Exercise Number)
def main():
    exercise8()
if __name__ == "__main__":
    main()