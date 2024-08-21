#* Write a program that asks for the number of kilometers traveled by a rented car and the number of days it was rented. Calculate the price to be paid, knowing that the car costs $60 per day and $0.15 per kilometer traveled.

days = int(input('How many days was the car rented? '))
km = float(input('How many kilometers did the car travel? '))

payment = (days * 60) + (km * 0.15)

print('The total amount to be paid is $ {:.2f}'.format(payment))