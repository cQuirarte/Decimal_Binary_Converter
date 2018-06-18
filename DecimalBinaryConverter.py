# Carlos Quirarte
# This program will help a user convert decimal values to binary
# The purpose of this program is to help network administrators


def convert():
    list1 = list()  # create an empty list
    iter = True     # used for iteration

    # while (iter):
    #     value1 = int(input("\nDecimal Value: "))  #This line causes error when entering a string rather than an int
    #     if (value1 > 255):
    #         print ("Enter a value less than 255 and greater than 0")
    #     elif (value1 < 0):
    #         print ("Enter a value less than 255 and greater than 0")
    #     else:
    #         iter = False

    while (iter):
        try:
            value1 = int(input("\nDecimal Value: "))
            print ("in 1")  # delete line after testing
            if (value1 > 255):
                print ("Enter a value less than 255 and greater than 0")
            elif (value1 < 0):
                print ("Enter a value less than 255 and greater than 0")
            else:
                iter = False
        except:
            print ("Please enter a number!")

    val1 = value1 # copy value1 content to val1

    # Algorithm to convert decimal to binary
    while (val1 >= 1):
        if (val1 % 2 == 0):
            list1.append(0)
        else:
            list1.append(1)
        val1 = val1 / 2
        val1 = int(val1)
    # Ensures that there are 8 total bits
    while (len(list1) < 8):
        list1.append(0)

    # Prints the values in reversed order, as it should be
    print ("Binary Value: " , end='')
    for item in reversed(list1):
        print(item, end='')
    print ("\n")

    # Ask user to run again
    again1 = input("Convert another value? (enter yes/no) ")
    if (again1 == "yes"):
        convert()           # Call on the function again to convert another value
    elif (again1 == "no"):
        print ("Program ended")


if __name__ == "__main__":
    print ("Decimal to Binary Converter\n")

    print ("Select an option")
    print ("1: Convert a single value to binary")
    print ("2: Convert an entire IP address based off IPv4")
    print ("0: Exit program")

    choice = int(input("\nYour choice: "))

    if (choice == 1):
        convert()
    elif (choice == 2):
        print ("2")
        convert()



