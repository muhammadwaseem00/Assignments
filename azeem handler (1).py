def start(): #program starts off from here
    print("Welcome to advanced calculations")
    A = int(input("Enter 1 to begin or press 2 to exit: ")) #User enters 1 of the provided options
    return A

def Actions(): #User has 5 options to select from, once they have select one option they will return here to select another
    print("Type 1 to convert integer -> decimal / 2 for subtract / 3 for addition / 4 for multiplier / 5 for floating point")
    B = int(input("Option: ")) #prompts the user to enter a number according to the options given above

    if B == 1: #Number corresponds to a function
        print("Loading the converter...")
        Conversion() #calls this function to convert decimal to binary
    elif B == 2:
        print("Loading...")
        Subtractor() #calls this function to subtract two decimal numbers and then convert to binary
    elif B == 3:
        print("Loading...")
        Addition() #calls this function 
    elif B == 4:
        print("Loading...")
        Multiplier() #Incompleted for other reasons
    elif B == 5:
        print("Loading...")
        Floating_Point() #Incompleted for other reasons
    else:
        print("Type the numbers specified")
        Actions()

def Conversion(): #Takes a integer number positive or negative and convert to binary
    Den = (int(input("Enter a number between -255 to 255: "))) #Den short for Denary or Decimal
    print (Den)
    if (Den > 256): #256; total of 8 binary digits (11111111)
        print ("Number between -255 to 255 please")
        Den = None #remove the recent input and restart the function
        Conversion()
    elif (Den < -256 ):
        print ("Number between -255 to 255 please")
        Den = None
        Conversion()
    else:
        print ("Processing...") #Presents our Denary number and converts into a Binary
        print ("In Decimal:" , Den) #or Denary but both Denary/Decimal have the same meaning
        print ("In Binary:" , "{0:0{1}b}".format(Den,8))
        print("Returning to option menu")
        Actions() #Return to option tab to select something else

def Addition(): #Enter two numbers which will add together and then convert into a binary 
    X = int(input("Enter a number between -255 to 255: ")) 
    if X < -256:
        print(X ,"is in range")
    elif X < 256:
        print(X ,"is in range")
    else:
        print("Follow the provided instructions") #we define X as nothing and restart the function, same applies with Y
        X = None
        Addition()

    Y = int(input("Enter a number between -255 to 255: "))
    if Y < -256:
        print(Y ,"is in range")
    elif Y < 256:
        print(Y ,"is in range")
    else:
        print("Follow the provided instructions")
        Y = None
        Addition()

    SUM = X + Y #We add our two successful inputs if they have met the criteria above and then take the SUM and convert to Binary
    print(SUM)
    
    print ("Processing...")
    print ("In Decimal:" ,SUM)
    print ("In Binary:" , "{0:0{1}b}".format(SUM,9)) #9 because the user might double number as high as 255 
    print("Returning to option menu")
    Actions() #Transfers back to the option tab to try something else out
    
def Subtractor(): #Similar process to the addition except it will subtract our two inputs instead 
    X = int(input("Enter a number between -255 to 255: ")) #provide a number between the given range
    if X < -256:
        print(X ,"is in range")
    elif X < 256:
        print(X ,"is in range")
    else:
        print("Follow the provided instructions")
        X = None
        Addition()

    Y = int(input("Enter a number between -255 to 255: "))
    if Y < -256:
        print(Y ,"is in range")
    elif Y < 256:
        print(Y ,"is in range")
    else:
        print("Follow the provided instructions")
        Y = None
        Addition()

    SUM = X - Y #Subtract our two successful inputs then convert its decimal format into binary
    print(SUM)
    
    print ("Processing...")
    print ("In Decimal:" ,SUM)
    print ("In Binary:" , "{0:0{1}b}".format(SUM,9))#9 because the user might double number as high as 255
    print("Returning to option menu")
    Actions()

def Multiplier():
    #I had the slightest of clue what this was about
    print("The function loads without problem")
    Actions()
    print("Returning to option menu")

def Floating_Point():
    Mantissa = int(input("Enter a number in binary (23 bits an 1 being the sign: "))
    Exponent = int(input("Enter a number in binary (8 bits): ")) 
    return Mantissa
    return Exponent
    print("Returning to option menu")
    Actions()

option = start()
    
if option == 1: #Based on what option we chose it follows accordingly
    print("Loading...")
    Actions() 
elif option == 2:
    print("Terminating program...")
    exit() #closes down the module (the execution phase)
else:
    print("What did you type?") #Just in case the user didnt type either 2 numbers
    start()
