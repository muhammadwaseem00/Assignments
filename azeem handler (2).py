def first_AND (A,B): #Works in the same principles of an AND gate
    print("Once this gate has been completed, return to solve the XOR gate")
    if A == 0 and B == 0: #Comparison of inputs A and B (00,10,01,11)
        AND = 0 #The output here will enter our OR gate
        print(A , " & " , B , " = " , AND)
        gate_path_A() #Returns to give us the opportunity to solve XOR gate
    elif A == 1 and B == 0:
        AND = 0
        print(A , " & " , B , " = " , AND) 
        gate_path_A()
    elif A == 0 and B == 1:
        AND = 0
        print(A , " & " , B , " = " , AND) 
        gate_path_A()
    elif A == 1 and B == 1:
        AND = 1 
        print(A , " & " , B , " = " , AND)
        gate_path_A()
    else: #Just incase negative integers or higher than 1 pass the program
        print("AND gate malfunctioned") 
 
def first_XOR (A,B): #operate on the principles of XOR gate 
    print("Once this gate has been completed, return to solve the AND gate")
    if A == 0 and B == 0: #Again compares inputs A and B (00,10,01,11)
        XOR = 0 #Output will enter the second XOR gate as well the second AND gate
        print(A , " ^ " , B , " = " , XOR) 
        gate_path_A() #We return so that we can move on (depends on which gate se solve first)
    elif A == 1 and B == 0:
        XOR = 1
        print(A , " ^ " , B , " = " , XOR) 
        gate_path_A()
    elif A == 0 and B == 1:
        XOR = 1
        print(A , " ^ " , B , " = " , XOR) 
        gate_path_A()
    elif A == 1 and B == 1:
        XOR = 0
        print(A , " ^ " , B , " = " , XOR) 
        gate_path_A()
    else: #Similar process as with the AND gate (acts as a safety measure)
        print("XOR gate malfunctioned")

def AND_MK2(XOR,PREV): #Operates like an AND gate but takes different inputs
    print("Once this gate has been completed, return to solve the XOR_MK2 gate")
    if XOR == 0 and PREV == 0: #Result of our first XOR gate and previous value
        AND_II = 0 #Previous value has no input so its automatically 0 hence only 2 possible combinations
        print(XOR , " & " , PREV , " = " , AND_II) 
        gate_path_B() #Returns so that we have a chance to solve the AND gate or move on
    elif XOR == 1 and PREV == 0:
        AND_II = 0 
        print(XOR , " & " , PREV , " = " , AND_II) 
        gate_path_B()
    else: #Again it is just incase something goes wrong 
        print("AND_MK2 gate malfunctioned")    

def XOR_MK2(XOR,PREV): #Similar operation to the first XOR gate and exact scenario with the AND MK2
    print("Once this gate has been completed, return to solve the AND_MK2 gate")
    if XOR == 0 and PREV == 0: #Only two possible inputs are possible 
        SUM = 0  #Output for one part of the Byte Adder
        print(XOR , " ^ " , PREV , " = " , SUM)
        gate_path_B ()
    elif XOR == 1 and PREV == 0:
        print(XOR , " XOR" , PREV , " = " , SUM)
        SUM = 1
        gate_path_B ()
    else: #If none of the above are processed
        print("XOR_MK2 gate malfunctioned")

def first_OR(AND,AND_II):#Works on the principles of an OR gate, it akes the outputs of our 2 AND gates 
    print("Byte Adder Complete and will return to the start") #Program completes and restarts
    if AND == 0 and AND_II == 0: #Outputs of our 2 AND gates the only possible combinations are 00, 10
        NEXT = 0 #stores the output in the variable NEXT
        print(AND , " | " , AND_II , " = " , NEXT)
        Bootup()
    elif AND == 1 and AND_II == 0:
        NEXT = 1
        print(AND , " | " , AND_II , " = " , NEXT)
        Bootup()
    else:
        print("first_OR gate malfunctioned")

def Bootup(): #Program starts from here onwards
    print ("Follow the instructions provided in this program")
    x = int(input("Type 1 to solve first set of gates or type 2 to exit: "))
    return x 

A = None #Define our input with nothing first of all
while A is None: #loop the program each time we havent entered either 1 or 0
    try:
        A = int(input("Enter a number 1 or 0: "))
    except ValueError:
        print("Did you read what the program stated?")
print(str(A)); #print the number we have typed

B = None
while B is None:
    try:
        B = int(input("Enter a number 1 or 0: "))
    except ValueError:
        print("Did you read what the program stated?")
print(str(B));

def gate_path_A (): #Loads when its called from the Bootup function
    print("Press 1 to solve AND gate or Press 2 to solve XOR gate or Press 3 to solve new set of gates")
    x = int(input("write 1/2/3: ")) #Type specified number from options above
    print("Loading...") #Calls the function according to the number typed
    if x == 1:
        first_AND(A,B)
    elif x == 2:
        first_XOR(A,B)
    elif x == 3:
        gate_path_B()
    else:
        print("Type a number 1,2 or 3")        
        gate_path_A()
        
PREV = None
while PREV is None:
    try:
        PREV = 0 
    except ValueError:
        print("Input is 0; we have nothing stored in the first place")
print("The only input for previous value is: " , PREV);

XOR = None
if A == 0 and B == 0: #Depends on what inputs A and B are
    XOR = 0
    print("The output from the first XOR gate is:" ,XOR)
elif A == 1 and B == 0:
    XOR = 1
    print("The output from the first XOR gate is:" ,XOR)
elif A == 0 and B == 1: 
    XOR = 1
    print("The output from the first XOR gate is:" ,XOR)
elif A == 1 and B == 1:
    XOR = 0
    print("The output from the first XOR gate is:" ,XOR)
else:
    print("Are you sure you stored input of 1 or 0?")

def gate_path_B(): #Operates the same way as the first gate path but new set of gates to solve
    print("Press 1 to solve AND_MK2 gate or Press 2 to solve XOR_MK2 gate or Press 3 to proceed the final gate")
    y = int(input("Type a number 1,2 or 3: "))
    print("Loading...")
    if y == 1: #Navigates based on what number was typed
        AND_MK2(XOR,PREV)
    elif y == 2:
        XOR_MK2(XOR,PREV)
    elif y == 3:
        gate_path_C()
    else:
        print("Type a number 1,2 or 3")
        gate_path_B()
        
AND = None
if A == 0 and B == 0: #Depends on what inputs A and B are
    AND = 0
    print("The output from the first AND gate is:" ,AND)
elif A == 1 and B == 0:
    AND = 0
    print("The output from the first AND gate is:" ,AND)
elif A == 0 and B == 1: 
    AND = 0
    print("The output from the first AND gate is:" ,AND)
elif A == 1 and B == 1:
    AND = 1
    print("The output from the first AND gate is:" ,AND)
else:
    print("Are you sure you stored inputs of 1 or 0?")

AND_II = None
if XOR == 0 and PREV == 0: #Depends on what the inputs of XOR and PREV are
    AND_II = 0
    print("The output from the second AND gate is:" ,AND_II)
elif XOR == 1 and PREV == 0:
    AND_II = 0
    print("The output from the second AND gate is:" ,AND_II)
else:
    print("Are you sure you stored inputs of 1 or 0?")
    
def gate_path_C(): #loads the final gate OR
    print("Loading OR gate which will store the result in variable called NEXT")
    first_OR(AND,AND_II)

Resume = 1
while Resume == 1: #loops until 1 of 2 numbers are entered.
   ALT = Bootup()
   if ALT == 1:
       print("Simulating Byte Adder...")
       gate_path_A()
   elif ALT == 2:
        print("Exiting Byte Adder")
        exit()
   else:
       print("Type a specified number")
       Bootup()

gate_path_A()
gate_path_B()
gate_path_C()
first_OR(AND,AND_II)
AND_MK2(XOR,PREV);
XOR_MK2(XOR,PREV);
first_AND(A,B)
first_XOR(A,B)
