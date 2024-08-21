#* Write a program who receives a temperature in Celsius and converts it to Fahrenheit

tempC = float(input("Enter the temperature in Celsius: "))

tempF = (tempC * 9 / 5) + 32

print("The temperature in Fahrenheit is: {:.2f}".format(tempF))