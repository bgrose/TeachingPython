import os.path

def runner():
    if(os.path.isfile('./file.txt') == True):
        f = open("./file.txt", "r")
        for x in f:
            print(x)
        f.close()

        f = open("./file.txt", "a")
        f.write("Hello, Midterm!")
        f.close()

        f = open("./file.txt", "r")
        for x in f:
            print(x)
        f.close()
    else:
        print("No file")
    

runner()