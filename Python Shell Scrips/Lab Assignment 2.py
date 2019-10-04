import math
# Albert Chang - LAB ASSIGNMENT 2
# Csc 11300 - 2N

############### Part A #######################################

def converted_minutes():
    milliseconds = float(input("Please enter the amount of minutes to convert into milliseconds: "))
    milliseconds = milliseconds * 60000
    print("The value of minutes to milliseconds is: ", milliseconds, "milliseconds")

############### Part B #######################################

def get_scores():
    x = float(input("Enter the first score: "))
    y = float(input("Enter the second score: "))
    return x,y

def get_average():
    a,b = get_scores()
    average = (a + b) / 2
    print("The average of the two scores is: ", average)

############### Part C #######################################

def get_values():
    a = float(input("Enter the a value: "))
    b = float(input("Enter the b value: "))
    c = float(input("Enter the c value: "))
    return a,b,c

def calculate_delta():
    try:
        x,y,z = get_values()
        delta = (y * y) - (4 * x * z)
        # y = y * (-1)
        x1 = ((-y + math.sqrt(delta)) / (2 * x))
        x2 = ((-y - math.sqrt(delta)) / (2 * x))

        print("The first root is: ", x1)
        print("The second root is ", x2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real root");
        else:
            print("Invalid inputs");

############### Part D #######################################

def Kelvin_Reaumur(k):
    Reaumur = (k - 273.15) * 0.8
    return Reaumur

def Reaumur_Celsius(a):
    Rea = Kelvin_Reaumur(a)
    celsius = Rea / 0.8
    return celsius

def printConverted_KRC():
    a = float(input("Please enter a value in kelvin to be converted to celsius: "))
    conversion = Reaumur_Celsius(a)
    print("The converted temperature in degrees celsius is: ", conversion, "°C")

############### Part E #######################################

def cube_size():
    n = float(input("Please input the length of side n of the cube: "))
    cubeSize = n**3
    marbleRadius = (n / 4)
    marbleVolume = (4/3) * math.pi * marbleRadius**3
    amount = cubeSize / marbleVolume
    print("The amount of marbles you can fit in the cube is:", int(amount), "marbles")

############### Part F #######################################
#Set number of columns for the grid
def columns(n):
    if n > 0:
        print("^ - ^ - ^", end="")
        n = n - 1
        if n == 0:
            print("^")
        return columns(n)

#Set number of i for edges based on number of columns
def i_grid(n):
    if n > 0:
        print("i        ", end="")
        n = n - 1
        if n == 0:
            print("")
        return i_grid(n)

#Generates the grid layout without the bottom border
def grid_generator(a):
    b = a
    if a > 0:
        columns(b)
        i_grid(b+1)
        i_grid(b+1)
        i_grid(b+1)
        i_grid(b+1)

def grid_output():
    # Adding more grid_generator(a) will result in additional rows
    # Increasing the value of the parameter will increase number of columns
    # NOTE: all the parameters should be the same value to generate proper grid

    grid_generator(4)
    grid_generator(4)
    grid_generator(4)
    grid_generator(4)

    #Used to complete the bottom border once grid generator is complete
    #NOTE: parameter must be the same value as parameter 'a' above
    columns(4)

############### CALL FUNCTIONS #########################
# Part A call function [WORKING PROPERLY]
# converted_minutes()

# Part B call function [WORKING PROPERLY]
# get_average()

# Part C call function [WORKING PROPERLY]
# calculate_delta()

# Part D Call function [WORKING PROPERLY]
# printConverted_KRC()

# Part E Call function [WORKING PROPERLY]
# cube_size()

# Part F Call function
# grid_output()
