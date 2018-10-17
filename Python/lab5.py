# Lab 5 - Randy Wu (040914510)
# Coded in python 3

from sense_hat import SenseHat

# The calcAlphaGrade function takes a number argument and checks it against a
# List of tuples, each element in the list contains a int and a letter grade.
# Using a for loop, the argument is checked if it is greater than or equal to
# The int in the tuple. If it is, the associated letter grade is returned, if
# Not, then the next int in the list is checked. And continues until it gets to
# The last element.

def calcAlphaGrade(numGrade):
    grades = [
        (89, "A+"),
        (85, "A"),
        (80, "A-"),
        (77, "B+"),
        (73, "B"),
        (70, "B-"),
        (67, "C+"),
        (63, "C"),
        (60, "C-"),
        (57, "D+"),
        (53, "D"),
        (50, "D-"),
        (0, "F"),
    ]
    for score in grades:
        if numGrade >= score[0] :
            return score[1]

# calcNumGrade takes 6 arguments, the weights of labs, midterms, and finals each
# A whole number (int and float supported). And the last 3 arguments are for
# The marks of labs, midterms, and finals. And the function outputs a number
# Mark based on the weights and marks of the individual.

def calcNumGrade(labWeight, midWeight, finalWeight, labMark, midMark, finalMark):
    grade = ((labWeight / 100) * labMark) + ((midWeight / 100) * midMark) + ((finalWeight / 100) * finalMark)
    return grade

# endingMessage takes 2 arguments, a numGrade number and a alphaGrade string.
# It checks if numGrade is a failng mark, and depending if it is or not. The
# Function will print out a appropriate message. If the mark is a passing grade
# The function will also show you the alphaGrade letter grade you passed with.

def endingMessage(numGrade, alphaGrade):
    if numGrade < 50:
        print ("\nYOU FAILED! LOOOOOSER")
    else:
        print ("\nCongratulations! You passed with a {}!".format(alphaGrade))

# welcomeMessage is a function that just prints the overly long welcome message
def welcomeMessage():
    print(
    """\n--Final Mark Calculator--

    Hello! Welcome to the super special awesome final mark calculator! This nifty thing
    will tell you the letter mark that you currently have by doing a whole bunch of mathy stuff!

    All you need to have on you is the weight of your labs, midterm and final, and then the actual
    mark of your labs, midterm, and final.

    When inputting the weights in, make sure to put in the whole number. So if your labs are worth
    40%, then put in 40 and not 0.4. numbers are No es bueno!

    For your marks do the same thing, if you have an 80, then input 80!

    Not 0.8,



    80,



    cool?



    COOL!

    Lets get popping!
    """
    )

# Creating the sense hat variable for later use.

hat = SenseHat()

welcomeMessage()

# The while true loop makes it so that the user can continue using the calculator
# Until they decide to stop.

choice = "y"
while choice == "y":

    labWeight = float(input("\nWhat is the weight of all of your labs?: "))
    labMark = float(input("\nWhat is the mark of all of your labs?: "))

    midWeight = float(input("\nWhat is the weight of of midterm?: "))
    midMark = float(input("\nWhat is the mark of of your midterm?: "))

    finalWeight = float(input("\nWhat is the weight of of your final?: "))
    finalMark = float(input("\nWhat is thle mark of of your final?: "))

    numGrade = calcNumGrade(labWeight, midWeight, finalWeight, labMark, midMark, finalMark)
    alphaGrade = calcAlphaGrade(numGrade)

    endingMessage(numGrade, alphaGrade)

# If numGrade is a passing mark, the sense hat will then display the alphaGrade.

    if numGrade >= 50:
        hat.show_message(alphaGrade, 0.2)

# The point where the user can choose if they want to continue or not. The loop
# Will continue unless the user inputs either "N" or "n".
    choice = input("\nWould you like to calculate another grade? (Please input either Y or N): ")
