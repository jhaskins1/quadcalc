#This program is a quadratic formula calculator
# ax^2 + bx + c
# x = ( -b +/- (b^2 - 4ac)^.5)/2a
from math import sqrt
from time import sleep
check1 = 1
while check1 == 1:
    check2 = 1
    print("Quadratic Formula Calculator")
    print()
    while check2 == 1:
        #Check if the user wants to re-eneter the equation
        print('''Based on this formula: ax² + bx + c . Enter values for each value, a , b, and c.
    If there is no number in front of the x, it is the value 1. If there is no term there, the value is 0.
    If the value is negative please include the '-' symbol in front of the value.''')
        print()
        #Have the user input numbers into an equation.
        a = input("Please enter a value for a: ")
        b = input("Please enter a value for b: ")
        c = input("Please enter a value for c: ")
        print("So your equation looks like this: " + a + "x² + " + b + "x + " + c + "? Say yes or no.")
        check3 = 1
        while check3 == 1:
            #Check if the user entered the correct equation
            correctEquation = input()
            if correctEquation == "Yes" or correctEquation == "yes":
                #If the user entered the right equation, move on.
                check2 = 0
                check3 = 0
            elif correctEquation == "No" or correctEquation == "no":
                #If the user entered the wrong equation, give them the option to re-enter it
                check2 = 1
                check3 = 0
            else:
                #If the user doesn't answer yes or no, ask again if its yes or no.
                print('Please say "yes" or say "no".')
            
    #Turn all the strings into decimals
    a = float(a)
    b = float(b)
    c = float(c)

    #Do the calculations for (-b + (b^2 - 4ac)^.5)/2a
    x1 = (b ** 2) - (4 * a * c)
    x1 = sqrt(x1)
    x1 = x1 + (-1 * b)
    x1 = x1/(2 * a)

    #Do the calculations for (-b - (b^2 - 4ac)^.5)/2a
    x2 = (b ** 2) - (4 * a * c)
    x2 = sqrt(x2)
    x2 = (-1 * b) - x2
    x2 = x2/(2 * a)

    #Print the solutions
    print("The solutions are " + str(x1) + " and " + str(x2))
    print('''

''')
    sleep(2)
    restart = input('''Would you like to use the calculator again?
If you would then enter 'yes' if not, don't enter anything. ''')
    if restart == "Yes" or restart == "yes":
        check1 = 1
    else:
        check1 = 0
