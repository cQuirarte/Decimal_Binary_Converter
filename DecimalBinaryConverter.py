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

    print ("in Convert function")   ### testing purposes

    # Convert val1 to str if int so we can iterate over it
    try:
        if (type(val1) == int):
            val1 = [val1]
            print ("test 34")
    except:
        pass

    # Algorithm to convert a decimal IP address to binary and store as list
    for v in range(0, len(val1)):

        # block of code for my testing purposes
        print ("test 2234")
        print ("length: ", len(val1))
        print ("val ", type(val1[v]))

        # Ensure each element is an int
        try:
            # if (type(val1[v]) == str):
            print (val1[v])
            # val1[v] = int(val1[v])
            print ("test 35")
        except:
            print ("fail 21")

        try:
            while (val1[v] >= 1):
                print ("test 111,  value[v] = ", val1[v])
                if (val1[v] % 2 == 0):
                    print ("insert 1/2")
                    list1.insert(0, 0)
                    print ("insert 1")
                else:
                    list1.insert(0, 1)
                    print ("insert 2")
                val1[v] = int(val1[v] / 2)      # Convert to int, dropping decimal point
            # Ensures that there are 8 total bits
            while (len(list1) < 8):
                print ("test 777")
                print ("val ", val1[v])
                list1.insert(0, 0)
                print (list1)
                print (list2)
            if (len(list1) == 8 and len(list2) == 27):
                print ("in here now")
                list2 += list1
                print (list2)
                break
            elif (len(list1) == 8 and len(val1) == 1):
                list2 += list1
        except:
            if (val1[v] == "."):
                print ("test 5533")
                list1.append(".")
                print (list1)
                list2 += list1

                print (list2)
                print ("test 2999")
                list1 = list()  # clear the list

        print ("test 998")
        t += 1
        print ("iteration ### ", t)
        if (t == 7):
            break
    print ("test 9333")

    # Display in binary after the converted
    displayBinary(list2)


# Prints the values of the array without space
def displayBinary(fullList):
    print ("Binary Value: " , end='')
    for item in (fullList):
        print(item, end='')
    print ("\n")


# Function to check if user's value is between 0 to 255
def betweenPar(usrNum):
    if (usrNum >= 0 and usrNum <= 255):
        print ("test 56")   # testing purposes
        return True
    elif (usrNum < 0 or usrNum > 255):  # testing purposes
        print ("test 57")
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
        ipAddress = list()
        tempList = list()
        octet = 0
        iter3 = 0
        again2 = True
        oct = 0
        k = 0

        print ("size of ipAddress " , len(ipAddress))

        try:
            while (again2):
                print ("k = ", k)
                print ("\nSeparate each octet by space or period")
                value2 = input("\nIP address: ") # get user input
                value2 += "."   ### used for the 'for loop' to add extra iteration
                print (value2, "length is ", len(value2))

                ipAddress = []  # Clear the list
                tempList = []

                # The for loop is not feasible. Stops short beucase it reaches last value of the string
                # and doesn't give the code below to run through and reach:
                #### might need to include a 'try except' here
                try:
                    for n in value2:
                        k += 1
                        print ("kk = ", k, " n=", n)
                        try:
                            n = int(n)  # Convert string element into an int
                            # if (isinstance(n, int)):  ### may delete
                            #     print ("testing")
                            tempList.append(str(n))
                            iter3 += 1 # testing purposes
                            print ("Iteration # ", iter3)
                            print ("test 955")    ### it stops here because 'for statement' reaches 7
                        except:
                            if (iter3 != 0 and (n == " " or n == ".")):
                                iter3 += 1 # testing purposes
                                print ("Iteration # ", iter3)
                                oct += 1        ### mainly useless might delete
                                # joining the array into a string / convert to str
                                octet = "".join(str(x) for x in tempList)
                                print ("# array joined successfully into string")
                                # convert to int
                                octet = int(octet)
                                print ("The octet is: ", octet)
                                if (betweenPar(octet)):
                                    print ("Pass: between 0 - 255")
                                    ipAddress.append(octet)
                                    print ("First octet appended to ipAddress, length ", len(ipAddress))
                                    if (len(ipAddress) < 7):  # number plus dot = 7 values
                                        print ("Pass, ipAddress <= 7")
                                        tempList = []  # clear the list
                                        ipAddress.append(".")
                                        print ("Cleared list, appended dot (.). Length now is ", len(ipAddress))
                                    elif (len(ipAddress) > 7):
                                        print("Error 1, should not be in here. write some code here")  ###### delete after
                                    elif (len(ipAddress) == 7):
                                            print("Iteration # ", iter3, "Final stage")
                                            finalData = ipAddress
                                            again2 = False
                                else:
                                    print ("\n! Please follow guidelines when entering the IP address")
                                    print ("! Enter IP address in the format example", style.BOLD + "255.255.255.255" + style.END)
                                    break
                            else:
                                print ("\n! Please follow guidelines when entering the IP address")
                                break
                        print ("Check 2")    ###### testing purposes
                    print ("length ", len(ipAddress))   ##### testing
                    if (len(ipAddress) < 7):
                        print ("\n! Enter 4 values representing the format for IP addressing", boldIP())
                    print ("test 9")
                except:
                    print ("fail 62")
        except:
            print("! fail 511")
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
                    print ("Pass first stage")
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
                    ### functin checkuserinput should return a value.
                    ipAddy = checkUserInput(2)
                    print ("Test 888")
                    print (ipAddy)
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
            print ("\n! Please enter a number option 2")

print ("-- Program ended --")