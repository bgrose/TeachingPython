def frontEnd():
    uInput = int(input("How many Items would you like to make"))
    dictionary = {}
    for x in range(uInput):
        key = "key" + str(x)
        value = "value" + str(x)
        dictionary[key] =  value
    print(dictionary)

frontEnd()
