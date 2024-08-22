import math

#*create a program that reads any Real number from the keyboard and displays its integer portion on the screen


num = float(input("Enter a number: "))

print("The integer portion of {} is {}".format(num, math.trunc(num)))
