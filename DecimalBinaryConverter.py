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
    displayBinary(list1) # Call on function to display binary conversion


# Prints the values in reversed order, as it should be
def displayBinary(fullList):
    print ("Binary Value: " , end='')
    for item in reversed(fullList):
        print(item, end='')
    print ("\n")

# Function to check if between 0 to 255
def betweenPar(usrNum):
    if (usrNum < 0 and usrNum > 255):
        return True
    else:
        return False



# Function to ensure user enters the appropriate responses i.e. "Please enter numbers not letters!"
def checkUserInput(data):
    # Convert single value option
    finalData = ""
    iter2 = True    # iterator
    again3 = "" # iterator

    if (data == 1):
        while (iter2):
            try:
                finalData = int(input("\nEnter Decimal Value: "))  # get user input
                # call function to check if between parameters
                iter2 = betweenPar(finalData)
            except:
                print ("Please enter a number!")
    # Convert IP option
    elif (data == 2):
        ipAddress = list()
        tempList = list()
        octet = 0
        iter3 = 0
        again2 = True

        try:
            while (again2):
                print ("\nSeparate each octet by space or period")
                value2 = input("\nIP address: ") # get user input
                print ("\n", value2)
                for n in value2:
                    # one for int the other for comma or space
                    # try:    ######## not done! finish
                        # val3 = int(n)
                    try:
                        n = int(n)  # Convert string element into an int
                        # if (isinstance(n, int)):  ### may delete
                        #     print ("testing")
                        tempList.append(str(n))
                        iter3 += 1 # might delete
                        print (iter3)
                            # elif (iter3 != 0 and (n == " " or n == ".")):
                            # print ("testing 2")
                            # octet = ''.join(tempList) # joing the numbers between the spaces into one
                            # # if (octet > 0 or octet < 255):
                            # if (betweenPar(octet)):
                            #     ipAddress.append(octet)
                            #     if (len(ipAddress) < 7):    # number plus dot = 7 values
                            #         tempList = []   # clear the list
                            #         ipAddress.append(".")
                            #     elif (len(ipAddress) == 7):
                            #         displayBinary(ipAddress)
                            #         break
                            # stop if number is not between parameters
                    except:
                        if (iter3 != 0 and (n == " " or n == ".")):
                            print ("testing 2")
                            # joing the numbers between the spaces into one
                            octet = "".join(str(x) for x in tempList)
                            print ("testing 3")
                            octet = int(octet)
                            print ("testing 4")
                            print (octet)
                            # if (octet > 0 or octet < 255):
                            if (betweenPar(octet)):
                                print ("testing 5")
                                ipAddress.append(octet)
                                if (len(ipAddress) < 7):  # number plus dot = 7 values
                                    tempList = []  # clear the list
                                    ipAddress.append(".")
                                elif (len(ipAddress) == 7):
                                    displayBinary(ipAddress)
                                    break
                                    #something else here to finish
                            else:
                                print ("Please follow guidelines when entering the IP address!")
                                break

                        else:
                            print ("Please follow guidelines when entering the IP address!")
                            break
                # print ("Convert another IP address? ")
                # if (again1 == "yes"):
                #     again3 = checkUserInput(3)
                # elif (again1 == "no"):
                #     again2 = False
        except:
            print("Please enter a valid IP address!")

    # Check that the user response is either 'yes' or 'no'
    elif (data == 3):
        while (iter2):
            finalData = input()
            # If answer is either yes or no then stop loop otherwise keep asking until accepted answer
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
    loop1 = True
    loop2 = True

    while (iter):
        #   main menu
        print("\nSelect an option")
        print("1: Convert a single value to binary")
        print("2: Convert an entire IP address based off IPv4")
        print("0: Exit program")

        try:
            choice = int(input("\nYour choice: "))
            if (choice == 1):
                while (loop1):
                    value = checkUserInput(choice)
                    convert(value)  # Call on convert() function

                    print ("Convert another value? (enter yes/no) ", end='')
                    again1 = checkUserInput(3)
                    # again1 = input("Convert another value? (enter yes/no) ")    #checkuserinput #might delete
                    if (again1 == "yes"):
                        continue    # just skip. keep loop1 True for reiteration
                        # convert()  # Call on the function again to convert another value #might delete line
                    elif (again1 == "no"):
                        loop1 = False
                        # print("Program ended")
            elif (choice == 2):
                while (loop2):
                    checkUserInput(2)
                    print("Convert another IP address? ")
                    again2 = checkUserInput(3)
                    if (again2 == "yes"):
                        continue    # just skip. keep loop2 True for reiteration
                    elif (again2 == "no"):
                        loop2 = False
            elif (choice == 0):
                iter = False    # end loop
                runProg = False # end program
            else:
                print ("Please enter a valid choice")
        except:
            print ("Please enter a number option!")


print ("-- Program ended --")





