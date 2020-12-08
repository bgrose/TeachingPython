import os

if os.path.isfile("file.txt"):
    file = open("file.txt", 'r+')
    line = file.read()
    print(line)
    file.write("\nHello, Midterm")
    line = file.read()
    print(line)
    file.close()
else:
    print("No File")