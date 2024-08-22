import math

#* Make a program that reads any angle and displays the value of its sine, cosine, and tangent on the screen.


angle = float(input("Enter an angle: "))

sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print("The sine of {} is {:.2f}".format(angle, sine))
print("The cosine of {} is {:.2f}".format(angle, cosine))
print("The tangent of {} is {:.2f}".format(angle, tangent))
