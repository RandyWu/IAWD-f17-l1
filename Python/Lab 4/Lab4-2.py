def convertGas(fuel, option):
    if option == 0 :
        converted_fuel = 235.21/fuel
        return ("{} US Miles per Gallon is also {} liters/100km".format(fuel, converted_fuel))
    else:
        converted_fuel = 235.21/fuel
        return ("{} Liters/100km is also {} US Miles per Gallon".format(fuel, converted_fuel))

print("Hello! Welcome to fuel efficiency converter! This is also going to be great!\n")
print("To use this amazing converter, just input the current fuel efficiency (as a float) you want to convert.\n")
print("And then input either 0 or 1.\n")
print("0 to convert from US MPG to L/100km, and 1 to convert from L/100km to US MPG.\n")
print("I feel like I've said this before, oh well, ONTO THE CONVERTING!\n")

input_fuel = float(raw_input("Please input your fuel efficiency to be converted as a float: "))
input_option = int(raw_input("\nWould you like to conver MPG to L/100km(0) or L/KM to MPG(1)?: "))

print(convertGas(input_fuel, input_option))
