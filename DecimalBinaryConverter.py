# Carlos Quirarte
# This program will help a user convert decimal values to binary
# The purpose of this program is to help network administrators


def convert(value1):
    list1 = list()  # create an empty list
    iter = True     # used for iteration

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
    # Call on function to display binary conversion
    displayBinary(list1)


# Prints the values in reversed order, as it should be
def displayBinary(fullList):
    print ("Binary Value: " , end='')
    for item in reversed(fullList):
        print(item, end='')
    print ("\n")


# Function to ensure user enters the appropriate responses i.e. "Please enter numbers not letters!"
def checkUserInput(data):
    # Convert single value option
    finalData = ""
    iter2 = True    # iterator

    if (data == 1):
        while (iter2):
            try:
                finalData = int(input("\nEnter Decimal Value: "))  # get user input
                if (finalData > 255):
                    print("Enter a value less than 255 and greater than 0!")
                elif (finalData < 0):
                    print("Enter a value less than 255 and greater than 0!")
                else:
                    iter2 = False
            except:
                print ("Please enter a number!")
    # Convert IP option
    elif (data == 2):
        try:
            value2 = input("\nIP address: ") # get user input
            ##### write code to use the dot as a dilimeter and convert string to int.
        except:
            print("Please enter a valid IP address!")
    # Check that the user response is either 'yes' or 'no'
    elif (data == 3):
        while (iter2):
            finalData = input("Convert another value? (enter yes/no) ")
            if (finalData == "yes" or finalData == "Yes" or finalData == "YES"):
                iter2 = False
            elif (finalData == "no" or finalData == "No" or finalData == "NO"):
                iter2 = False
            else:
                print ("Please respond by either 'yes' or 'no'\n")

    return finalData


if __name__ == "__main__":
    print ("Decimal to Binary Converter")
    iter = True     # iterator for main menu option

    while (iter):
        #   main menu
        print("\nSelect an option")
        print("1: Convert a single value to binary")
        print("2: Convert an entire IP address based off IPv4")
        print("0: Exit program")

        try:
            choice = int(input("\nYour choice: "))
            if (choice == 1):
                loop1 = True    # iterator
                # Ask user to run the function again
                while (loop1):
                    value = checkUserInput(choice)
                    convert(value)  # Call on convert() function
                    again1 = checkUserInput(3)
                    # again1 = input("Convert another value? (enter yes/no) ")    #checkuserinput #might delete
                    if (again1 == "yes"):
                        continue    # just skip. keep loop1 True for reiteration
                        # convert()  # Call on the function again to convert another value #might delete line
                    elif (again1 == "no"):
                        loop1 = False
                        # print("Program ended")
            elif (choice == 2):
                print ("2")
                convert()
            elif (choice == 0):
                iter = False    # end loop
                runProg = False # end program
        except:
            print ("Please enter a number option!")


print ("-- Program ended --")





