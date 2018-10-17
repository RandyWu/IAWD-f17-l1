# Coded in python3
import csv

# The create_csv function takes the name of the file you want to open, the name
# of the file you want to write too, and the column names of the csv file as arguments.
# It then opens the file name with the csv.reader and splits all the values and creates
# a list using list comprehension. Then takes the list and converts it into a dictionary.
# A csv string (format "x , y") is then created using the key and value of the dict
# and then written to the csv file.
def create_csv(file_name, csv_file_name, column_names):
    read_file = csv.reader(open(file_name))
    csv_writeout = open(csv_file_name, "w")
    csv_writeout.write(column_names)

    item_list = [item.split(" ") for row_elements in read_file for item in row_elements]
    item_dict = {first_name : count for first_name, count in item_list}

    for key in item_dict:
        first_name = key
        count = item_dict[key]
        row = first_name + "," + count + "\n"
        csv_writeout.write(row)

    csv_writeout.close()

# Function takes the name of the file you want to open and returns it as a dictionary
# representation.
def read_csv (file_name):
    read_file = csv.reader(open(file_name))
    final_dict = dict(read_file)
    return (final_dict)

create_csv("2000_BoysNames.txt", "2000_BoysNames.csv", "First Name, Count\n")
create_csv("2000_GirlsNames.txt", "2000_GirlsNames.csv", "First Name, Count\n")

# While loop such that the user can continue or end whenever they please.
choice = "Y"
while (choice == "Y" or choice == "y"):
    file_name = input("\nWhat is the name of the file that you want to open?(Please include the extension) ")
    dict_display = read_csv(file_name)

    for key in dict_display:
        print (key + " " + dict_display[key])

    choice = input("\nWould you like to read another file? (Please input either 'y' or 'n') ")
