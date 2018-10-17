from sense_hat import SenseHat

hat = SenseHat()
hat_temp = hat.get_temperature()

converted_temp = (hat_temp * 1.8) + 32

print ("The sense hat says that it is currently {} celsius which is also {} fahrenheit".format(hat_temp,converted_temp))

hat.show_message(str(converted_temp), text_colour=[255,255,0], back_colour=[139,0,139])
hat.clear()
