import math

def computeDistance(x, y, x1, y1):
    distance = math.hypot(x1-x, y1-y)
    return distance

print("hi again, this is the amazing distance calculator blah blah.\n")
print("just input your coordinates in one by one.\n")
print("it will follow (input1,input2) and (input3,input4).\n")
print("and it will give you a distance or like whatever.\n")

cor1 = int(raw_input("What is your first point?: "))
cor2 = int(raw_input("\nand the second?: "))
cor3 = int(raw_input("\nand the third?: "))
cor4 = int(raw_input("\nyou get it: "))

print ("The distance is {}....yaaaaaay".format(computeDistance(cor1,cor2,cor3,cor4)))
