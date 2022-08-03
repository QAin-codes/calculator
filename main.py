#Quratul Ain
#july 2022
#calculator
#global number1,number2

def menuOptions2():
    options = 0 # creating a flag variable and initialize it with zero
    
    while options not in ["1","2","3","4","5"]:
        print("\ Select the mathematical operation to be performed: \nEnter \n1. To Addition. \n2. To Substract. \n3. To Multiply. \n4. To Divide. \n5. Exit. ")
    #re-assaign the option variable to an input function 
        options = input("\n Enter any one of the options above: ")
        # check user input with the items in the list
        if options  not in ["1","2","3","4","5"]:
            print(f"{options} is not a valid choice!")
    return options
 
mainProgram = True # assaign main program a boolean datatype

# name ="jane"
# while name==jane ... do this
while mainProgram ==True: #checking if main program is equals to true
    mainmenu = menuOptions2() # we are passing memuoptions to a variable
    # if options(1/2/3/4/5) call the specific function/subroutine
    if mainmenu == "1": 
        num1=int(input("Please enter the first value :"))
        num2=int(input("Please enter the second value :"))# ifthe user inputis equal to option 1 in the list
        num3 = num1+num2
        print(num3)
    elif mainmenu =="2":
        num1=int(input("Please enter the first value :"))
        num2=int(input("Please enter the second value :"))
        num3 = num1-num2
        print(num3)
    elif mainmenu =="3":
        num1=int(input("Please enter the first value :"))
        num2=int(input("Please enter the second value :"))
        num3 = num1*num2
        print(num3)
    elif mainmenu =="4":
        num1=int(input("Please enter the first value :"))
        num2=int(input("Please enter the second value :"))
        num3 = num1/num2
        print(num3)
    else:
        mainProgram = False


 