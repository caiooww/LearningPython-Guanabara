#* Make a program that reads the width and height of a wall in meters, calculates its area, and the amount of paint needed to paint it, knowing that each liter of paint covers an area of 2m^2.

width = float(input("Enter the width of the wall: "))
height = float(input("Enter the height of the wall: "))

area = width * height
paint = area / 2

print(f"You will need {paint:.2f} liters of paint")