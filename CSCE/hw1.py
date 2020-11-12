def write_to_file(file_name, data):
    fileOut = open(file_name, "a")
    fileOut.write(data)
    fileOut.write("\n")
    fileOut.close


def read_from_file(file_name):
    fileIn = open(file_name)
    line = fileIn.read()
    print(line)

def ask_user():     
    answer = input("Type \"read\" or  \"write\":    ")
    if answer == "read":
        file = input("What is the file name:    ")
        read_from_file(file)

    elif answer == "write":
        file = input("What is the file name:    ")
        data = input("What data should I add:   ")
        write_to_file(file, data)
