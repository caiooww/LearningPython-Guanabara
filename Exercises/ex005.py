#*Create a program that reads an integer number and displays its predecessor and successor on the screen

value = int(input("Enter a value: "))

print("The predecessor of {} is {}, and the successor of {} is {}".format(value, value - 1, value, value + 1))