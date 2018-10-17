# Randy Wu 040914510 CST8279
# Coded in Python 3

import re

# Takes the first letter and number of a postal code, and a dict as arguments.
#Checks to see if letter is in the dict, and if number is == 0 or >= 1. Returns
# the appropriate string if valid, if invalid, returns the appropriate string.
def province_detector(letter, number,province_dict):
    if (letter in province_dict and number == 0):
        result_string = "The postal code is in rural " + province_dict[letter]
    elif (letter in province_dict and number >= 1):
        result_string = "The postal code is in urban " + province_dict[letter]
    else:
        result_string = "Please enter a valid postal code"

    return result_string

# Takes a postal code, and a dict as arguments. Checks if the postal is len of 7
# or if the first letter is in the dict. If not, returns false, else true.
def postal_validator(string, province_dict):
    if len(string) != 7:
        return False
    elif string[:1] not in province_dict:
        return False
    else:
        return True

province_dict = {
    "A" : "Newfoundland",
    "B" : "Nova Scotia",
    "C" : "P.E.I",
    "E" : "New Brunswick",
    "G" : "Quebec",
    "H" : "Quebec",
    "J" : "Quebec",
    "K" : "Ontario",
    "L" : "Ontario",
    "M" : "Ontario",
    "N" : "Ontario",
    "P" : "Ontario",
    "R" : "Manitoba",
    "S" : "Saskatechewan",
    "T" : "Alberta",
    "V" : "British Columbia",
    "X" : "Nunavut or the NW Territories",
    "Y" : "Yukon",
}

choice = "y"
while (choice == "y" or choice == "Y"):

    postal_code = input("Please input a postal code (format 'A1B 2C3'): ").upper()

    if (postal_validator(postal_code, province_dict)):
        first_letter = re.findall("[A-Z]", postal_code)[0]
        first_number = int(re.findall("[0-9]", postal_code)[0])

        print (province_detector(first_letter, first_number, province_dict))
        choice = input("\nWould you like to input another postal code? (Y or y): ")

    else:
        print ("Please input a valid postal code")
        choice = input("\nWould you like to input another postal code? (Y or y): ")

#split and replace
#split_string = postal_code[:2].replace(""." ")
#first_letter = split_string[1]
#first_number = int(split_String[3])

#list
#list_string = list(postal_code)
