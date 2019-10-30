# Question 1
def determinePerfectNum():
    try:
        value = int(input("Please enter a positive integer to check if it is a perfect number >> "))
        sum = 0
        for i in range(1, value):
            if value % i == 0:
                sum += i
        if sum == value:
            print("The value inputted is indeed a perfect number!")
        else:
            print("The value inputted is not a perfect number!")
    except ValueError:
        print("The value you inputted is not an integer!")

# Question 2
def positiveIntDivisors():
    looping = "yes"
    while looping[0] == 'y':
        value = int(input("Please enter a positive integer to find all the positive integer divisors >> "))
        sum = 0
        for i in range(1, value):
            if value % i == 0:
                print(i)
                sum += i
        looping = input("Would you like to perform this method again? Yes or no? >> ")

# Question 3
def checkIfTriangle():
    looping = "yes"
    while looping[0] == 'y':
        try:
            # Gathers the inputted points
            x1 = float(input("Enter coordinates for the first x point >> "))
            y1 = float(input("Enter coordinates for the first y point >> "))
            x2 = float(input("Enter coordinates for the second x point >> "))
            y2 = float(input("Enter coordinates for the second y point >> "))
            x3 = float(input("Enter coordinates for the third x point >> "))
            y3 = float(input("Enter coordinates for the third y point >> "))

            areaOfPoints = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

            # Area will be calculated. If area = 0, a triangle is not possible
            if areaOfPoints == 0:
                print("The points inputted does not form a triangle!")
            else:
                print("The points inputted form a triangle!")
        except ValueError:
            print("Invalid input. Coordinates inputted must be numbers.")
        looping = input("Would you like to perform this method again? Yes or no? >> ")

# Question 4
def primeBetweenInterval():
    print("This function will list all the prime numbers in between the given intervals you provide...")
    looping = "yes"
    while looping[0] == 'y':
        try:
            beginning = int(input("Please enter the beginning of the interval >> "))
            ending = int(input("Please enter the ending of the interval >> "))

            for value in range(beginning, ending + 1):
               if value > 1:
                   for i in range(2, value):
                       if (value % i) == 0:
                           break
                   else:
                       print(value)
        except ValueError:
            print("Invalid input. Values inputted must be integers.")
        looping = input("Would you like to run this function again? Yes or no? >> ")

# Question 5
def seatingArangements():
    looping = "yes"
    while looping[0] == 'y':
        try:
            totalNumOfPeople = int(input("Please enter the total number of people present >> "))
            peopleSeated = int(input("Please enter the total number of people that will be seated >> "))
            seatsArranged = 1
            # The number of people being seated must not be more than the total amount of people present
            assert(peopleSeated < totalNumOfPeople)
            while peopleSeated < (totalNumOfPeople + 1):
                seatsArranged *= peopleSeated
                peopleSeated += 1
            print("The number of possible seating arrangements is", seatsArranged)
        except ValueError:
            print("Invalid input. Values inputted must be integers.")
        except AssertionError:
            print("The number of people seated cannot be greater than the total amount of people present!!!")
        looping = input("Would you like to run this function again? Yes or no? >> ")

# Question 1
# determinePerfectNum()

# Question 2
# positiveIntDivisors()

# Question 3
# checkIfTriangle()

# Question 4
# primeBetweenInterval()

# Question 5
# seatingArangements()
