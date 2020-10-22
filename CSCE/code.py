
name = input("Please Enter Your Name: ")
address = input("Please Enter Your Street Address: ")
city = input("Please Enter Your City and State: ")
phone = input("Please Enter Your Phone Number: ")

fileOut = open("contact.txt", "w")
fileOut.write(name + "\n" + address + "\n" + city + "\n" + phone)
fileOut.close
