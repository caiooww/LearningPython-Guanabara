# sum +
# sub -
# mult *
# div /
# mod %
# pow **
# floor division //
# percent %
# compare ==, >, <, >=, <=, !=


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("The sum between {} and {} is {}".format(n1, n2, n1 + n2))

print("The sub between {} and {} is {}".format(n1, n2, n1 - n2))

print("The mult between {} and {} is {}".format(n1, n2, n1 * n2))

print("The div between {} and {} is {}".format(n1, n2, n1 / n2))

print("The mod between {} and {} is {}".format(n1, n2, n1 % n2))

print("The pow between {} and {} is {}".format(n1, n2, n1 ** n2))

print("The floor div between {} and {} is {}".format(n1, n2, n1 // n2))

print("The percent between {} and {} is {}".format(n1, n2, n1 % n2))

print("Is {} equal to {}? {}".format(n1, n2, n1 == n2))

print("Is {} greater than {}? {}".format(n1, n2, n1 > n2))

print("Is {} less than {}? {}".format(n1, n2, n1 < n2))

print("Is {} greater or equal than {}? {}".format(n1, n2, n1 >= n2))

print("Is {} less or equal than {}? {}".format(n1, n2, n1 <= n2))

print("Is {} not equal to {}? {}".format(n1, n2, n1 != n2))

#correct precedence
# 1. ()
# 2. **
# 3. * / // %
# 4. + -