
#* Make a program that reads the length of the opposite side and the adjacent side of a right triangle. Calculate and show the length of the hypotenuse.

import math

opposite_side = float(input("Enter the length of the opposite side: "))
adjacent_side = float(input("Enter the length of the adjacent side: "))

hypotenuse = math.hypot(opposite_side, adjacent_side)

print("The length of the hypotenuse is: {:.2f}".format(hypotenuse))
