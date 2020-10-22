fileIn = open("text1.txt")
string = fileIn.read(5)
print(string)
fileIn.close

fileOut = open("text2.txt", "w")
fileOut.write("I hate this class")
fileOut.close

