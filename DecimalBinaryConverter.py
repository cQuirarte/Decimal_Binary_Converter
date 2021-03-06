# Carlos Quirarte
# Created 2018
# The purpose of this program is to help network administrators
# convert single decimal values or an entire IP address into binary.


class style:
   BOLD = '\033[1m'
   END = '\033[0m'


def convert(value1):
    list1 = list()  # create an empty list
    list2 = list()
    iter = True     # used for iteration
    t = 0
    val1 = value1 # copy value1 content to val1
    # Convert val1 to str if int so we can iterate over it
    try:
        if (type(val1) == int):
            val1 = [val1]
    except:
        pass

    # Algorithm to convert a decimal IP address to binary and store as list
    for v in range(0, len(val1)):
        try:
            while (val1[v] >= 1):
                if (val1[v] % 2 == 0):
                    list1.insert(0, 0)
                else:
                    list1.insert(0, 1)
                val1[v] = int(val1[v] / 2)      # Convert to int, dropping decimal point
            # Ensures that there are 8 total bits
            while (len(list1) < 8):
                list1.insert(0, 0)
            if (len(list1) == 8 and len(list2) == 27):
                list2 += list1
                break
            elif (len(list1) == 8 and len(val1) == 1):
                list2 += list1
        except:
            if (val1[v] == "."):
                list1.append(".")
                list2 += list1
                list1 = list()  # clear the list
        t += 1
        if (t == 7):
            break
    # Display in binary after the converted
    displayBinary(list2)


# Prints the values of the array without space
def displayBinary(fullList):
    print ("\nBinary Value: " , end='')
    for item in (fullList):
        print(item, end='')
    print ("\n")


# Function to check if user's value is between 0 to 255
def betweenPar(usrNum):
    if (usrNum >= 0 and usrNum <= 255):
        return True
    elif (usrNum < 0 or usrNum > 255):  # testing purposes
        return False


def boldIP():
    return (style.BOLD + "255.255.255.255" + style.END)


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
                if (betweenPar(finalData)):
                    iter2 = False
                else:
                    print ("\n! Please enter a value from 0 to 255")
            except:
                print ("\n! Please enter a value from 0 to 255")
    # Convert IP option
    elif (data == 2):
        iter3 = 0
        again2 = True
        try:
            while (again2):
                print ("\nSeparate each octet by period or space")
                value2 = input("\nIP address: ") # get user input
                value2 += "."   ### used for the 'for loop' to add extra iteration
                # Initialize and clear the lists
                ipAddress = []
                tempList = []

                try:
                    for n in value2:
                        try:
                            n = int(n)  # Convert string element into an int
                            tempList.append(str(n))
                            iter3 += 1 # iteration purposes
                        except:
                            if (iter3 != 0 and (n == " " or n == ".")):
                                iter3 += 1 # iteration purposes
                                # joining the array into a string / convert to str
                                octet = "".join(str(x) for x in tempList)
                                # Convert from str to int. Also drops extra 0s '0000'-> 0
                                octet = int(octet)
                                if (betweenPar(octet)):
                                    ipAddress.append(octet)
                                    if (len(ipAddress) < 7):  # number plus dot = 7 values
                                        tempList = []  # clear the list
                                        ipAddress.append(".")
                                    elif (len(ipAddress) > 7):
                                        print("Error 261")  ###### delete after
                                    elif (len(ipAddress) == 7):
                                            finalData = ipAddress
                                            again2 = False
                                else:
                                    print ("\n! Please follow guidelines when entering the IP address")
                                    print ("\n! Enter IP address in the format example", style.BOLD + "255.255.255.255" + style.END)
                                    break
                            else:
                                print ("\n! Please follow guidelines when entering the IP address")
                                break
                    if (len(ipAddress) < 7):
                        print ("\n! Enter 4 values representing the format for IP addressing", boldIP())
                except:
                    print ("Error 626")
        except:
            print("Error 677")
    # Check that the user response is either 'yes' or 'no'
    elif (data == 3):
        while (iter2):
            finalData = input()         ##### NEEDS error control !! FIX THIS!
            # If answer is either yes or no then stop loop otherwise keep asking until accepted answer
            if (finalData == "yes" or finalData == "Yes" or finalData == "YES"):
                iter2 = False
            elif (finalData == "no" or finalData == "No" or finalData == "NO"):
                iter2 = False
            else:
                print ("\n! Please respond either 'yes' or 'no'\n")
    return finalData


if __name__ == "__main__":
    print ("Decimal to Binary Converter")
    iter = True     # iterator for main menu option
    loop1 = True
    loop2 = True

    while (iter):
        loop1 = True
        loop2 = True
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
                    if (again1 == "yes"):
                        continue    # just skip. keep loop1 True for reiteration
                    elif (again1 == "no"):
                        loop1 = False
            elif (choice == 2):
                while (loop2):
                    ### functin checkuserinput should return a value.
                    ipAddy = checkUserInput(2)
                    convert(ipAddy)
                    print("Convert another IP address? (enter yes/no) ", end='')
                    again2 = checkUserInput(3)
                    if (again2 == "yes"):
                        continue    # just skip. keep loop2 True for reiteration
                    elif (again2 == "no"):
                        loop2 = False
            elif (choice == 0):
                iter = False    # end loop
                runProg = False # end program
            else:
                print ("\n! Please enter a valid choice")
        except:
            print ("\n! Please enter a number option")

print ("\n-- Program ended --")