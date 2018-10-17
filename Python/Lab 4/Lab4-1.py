def convertTemperature(temp, option):
    if option == 0:
        converted_temp = (temp - 32) / 1.8
        return "{} is also {} celsius".format(temp, converted_temp)
    else:
        converted_temp = (temp * 1.8) + 32
        return "{} is also {} fahrenheit".format(temp, converted_temp)

print("Hello! Welcome to temperature converter! This is going to be great!\n")
print("To use this amazing converter, just input the temperature (as an int!) you want to convert.\n")
print("And then input either 0 or 1.\n")
print("0 to convert from fahrenheit to celsius, and 1 to convert from celsius to fahrenheit.\n")

input_temp = int(raw_input("Please enter your desired temperature to be converted: "))
input_option = int(raw_input("\nWould you like to convert to fahrenheit(0) or celsius(1)?: "))

print (convertTemperature(input_temp, input_option ))
