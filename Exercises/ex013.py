#* Make an algorithm that reads an employee's salary and shows their new salary, with a 15% increase

salary = float(input("Enter the salary: "))

newSalary = salary * 1.15

print("The new salary with a 15% increase is: $ {:.2f}".format(newSalary))