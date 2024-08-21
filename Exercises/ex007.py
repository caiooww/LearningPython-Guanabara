#*Create a program that reads two grades from a student and calculates and displays their average

n1 = int(input('Enter the first grade: '))
n2 = int(input('Enter the second grade: '))
average = (n1 + n2) / 2

print('The average of the grades between {} and {} is: {}'.format(n1, n2, average))