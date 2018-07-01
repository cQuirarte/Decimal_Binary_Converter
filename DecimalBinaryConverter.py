# Carlos Quirarte
# This program will help a user convert decimal values to binary
# The purpose of this program is to help network administrators

import types

def convert(value1):
    list1 = list()  # create an empty list
    list2 = list()
    iter = True     # used for iteration
    t = 0
    val1 = value1 # copy value1 content to val1

    print ("in Convert function")

    # Convert val1 to str if int so we can iterate over it
    try:
        if (type(val1) == int):
            val1 = [val1]
            print ("test 34")
    except:
        pass


    # if (isinstance(val1, list)):
    #     for v in val1:
    #         try:
    #             while (v >= 1):
    #                 if (v % 2 == 0):
    #                     list1.append(0)
    #                 else:
    #                     list1.append(1)
    #             v = v / 2
    #         except:
    #             if (v == "."):
    #                 list.append(".")
    ###### need to revise the below code to accomodate not only an int but also a list.
    #####   might have to work with 2 lists. Upon reaching ".", add that, and add (+) the 2 lists.

    # Code to convert a decimal IP address to binary and store as list
    for v in range(0, len(val1)):
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
                val1[v] = val1[v] / 2
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
                # displayBinary(list1) # Call on function to display binary conversion  # may delete

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

    displayBinary(list2)

    #### keep, might need it
    # try:
    #     # if val1 is a single int value
    #     while (val1 >= 1):
    #         if (val1 % 2 == 0):
    #             list1.append(0)
    #         else:
    #             list1.append(1)
    #         val1 = val1 / 2
    #         val1 = int(val1)
    #     # Ensures that there are 8 total bits
    #     while (len(list1) < 8):
    #         list1.append(0)
    #     displayBinary(list1) # Call on function to display binary conversion
    # except:
    #     ### finish writing code
    #     # continue
    #     for v in val1:
    #         try:
    #             continue
    #         except:
    #             continue


# Prints the values in reversed order, as it should be
def displayBinary(fullList):
    print ("Binary Value: " , end='')
    for item in (fullList):
        print(item, end='')
    print ("\n")


# Function to check if between 0 to 255
def betweenPar(usrNum):
    if (usrNum >= 0 and usrNum <= 255):
        return True
    elif (usrNum < 0 and usrNum > 255):
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
                if (betweenPar(finalData)):
                    iter2 = False
            except:
                print ("Please enter a number! 3")
    # Convert IP option
    elif (data == 2):
        ipAddress = list()
        tempList = list()
        octet = 0
        iter3 = 0
        again2 = True
        oct = 0

        print ("size of ipAddress " , len(ipAddress))

        try:
            while (again2):
                print ("\nSeparate each octet by space or period")
                value2 = input("\nIP address: ") # get user input
                value2 += "."
                print (value2)

                # The for loop is not feasible. Stops short beucase it reaches last value of the string
                # and doesn't give the code below to run through and reach:
                for n in value2:
                    try:
                        n = int(n)  # Convert string element into an int
                        # if (isinstance(n, int)):  ### may delete
                        #     print ("testing")
                        tempList.append(str(n))
                        iter3 += 1 # testing purposes
                        print ("Iteration # ", iter3)
                        print ("in try")    ### it stops here because for statement reaches 7
                    except:
                        if (iter3 != 0 and (n == " " or n == ".")):
                            iter3 += 1 # testing purposes
                            print ("Iteration # ", iter3)
                            oct += 1
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
                                print ("Please follow guidelines when entering the IP address!")
                                print ("Should prompt user to continue. Avoid entering loop...'Separate each octet by space...")
                                break
                        else:
                            print ("Please follow guidelines when entering the IP address!")
                            break
                    # write some code here, maybe just 'continue' or delete line after you know that "break"
                    # allows for the interpreter to flow through here.
                    print ("Check 2")    ###### delete after taken care of

                ### This code belongs within the for loop to complete the IP address
                # if (len(ipAddress == 6)):         !!!!
                #     ipAddress.append(octet)
                #     print ("Iteration # ", iter3, "Final stage")
                #     convert(ipAddress)

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
            print ("Please enter a number option! 2")

print ("-- Program ended --")