
# Takes a list argument and returns a boolean depending if the argument is sorted
# or not. The function sorts the given list and checks it against the original list.
# If they are eqal it will then return true, else false. The function would also
# work if given a string of char, as the sorted() function is magical and also
# sorts letters.
def isSorted(my_list):
    if sorted(my_list) == my_list:
        return True;
    else:
        return False;

# Takes two string arguments and returns a boolean depding if the arguments are
# an anagram. The function sorts both arguments and compares them, if they are
# the same, then by definition the strings are an anagram and thus true, else
# false.
def isAnagram(base_string, compare_string):
    if sorted(compare_string) == sorted(base_string):
        return True;
    else:
        return False;

# Takes a list argument and returns a list consisting of all unique elements from
# the argument. The function removes all duplicates by getting the set of the
# argument (set(my_list)). And then creates a list of the set of the argument
# (list(set(my_list))), which then gives a unordered list of unique elements.
# The set function is a built in python function that gathers all unique elements
#
def removeDuplicates(my_list):
    no_dupe = list(set(my_list))
    return no_dupe

# Takes a list argument and returns a list of all elements squared. The function
# uses a list comprehension (a python exclusive feature to easily create lists).
# The list comprehension is the equivalent of doing:
#
#    new_list = []
#    for element in my_list:
#        new_list.append(element ** 2)
#    total_sum = sum(new_list)
#    return total_sum
#
def sumOfSquare(my_list):
    return sum([element ** 2 for element in my_list])


# Takes no arguments. The function asks the user for a number and returns the
# input while displaying instructions for the user.
def mainMenu():
    choice = int(
        input (
        """
        Hello!

        Welcome to lab 7! Please input which function you would like to test:
        1)Sorted list test
        2)Anagram test
        3)Duplicate test
        4)Sum of squares test

        """
        )
    )
    return choice


while True:
    choice = mainMenu()

# new_list is using a list comprehension to generate a result list. The
# list comprehension is equivalent to:
#    new_list = []
#    for user_input in input("Please enter numbers seperated by spaces (ex: 1 2 3 4 will give [1,2,3,4]): ").split():
#        new_list.append(int(user_input))
    if choice == 1:
        new_list = [
            int(user_input) for user_input in input(
            "Please enter numbers seperated by spaces (ex: 1 2 3 4 will give [1,2,3,4]): ").split()
        ]
        result = isSorted(new_list)
        if result == True:
            print ("The list you gave is sorted")
        else:
            print ("The list you gave is not sorted")

        continue_choice = input("Would you like to continue? Please input either y or n: ")
        if continue_choice == 'N' or continue_choice == 'n':
            break;


# The stripped_base and stripped_compare use the join function to eliminate
# All whitespace from the user input. Such that an input of " Hello W or l d"
# would be stripped down to "HelloWorld"
    elif choice == 2:
        base_string = input("Please input a string (case sensitive): ")
        compare_string = input("Please input a string to compare with (case sensitive): ")
        stripped_base = "".join(base_string.split())
        stripped_compare = "".join(compare_string.split())

        result = isAnagram(stripped_base, stripped_compare)

        if result == True:
            print ("The string you gave is an anagram for: {}".format(base_string))
        else:
            print ("The string you gave is not an anagram for: {}".format(base_string))

        continue_choice = input("Would you like to continue? Please input either y or n: ")
        if continue_choice == 'N' or continue_choice == 'n':
            break;


    elif choice == 3:
        base_string = input("Please input a string: ")
        result = removeDuplicates(base_string)

        print ("This is your string without any duplicates: {}".format(result))

        continue_choice = input("Would you like to continue? Please input either y or n: ")
        if continue_choice == 'N' or continue_choice == 'n':
            break;

# Same as in choice 1, new_list is using a list comprehension to create a result
# list. The list comprehension is the equivalent of doing:
#     new_list = []
#     for user_input in input("Please enter seperated by spaces (ex: 1 2 3 4 will give [1,2,3,4]): ").split():
#         new_list.append(int(user_input))
    elif choice == 4:
        new_list = [int(user_input) for user_input in input("Please enter numbers seperated by spaces (ex: 1 2 3 4 will give [1,2,3,4]): ").split()]

        result = sumOfSquare(new_list)
        print ("This is the sum of your list squared: {}".format(result))

        continue_choice = input("Would you like to continue? Please input either y or n: ")
        if continue_choice == 'N' or continue_choice == 'n':
            break;
