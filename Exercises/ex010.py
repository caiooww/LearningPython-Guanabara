#* Create a program that reads how much money a person has and how many dollars they can spend
#?Considering the dollar at 5.30 reais

money = float(input("Enter how much money you have: "))
dollar = money / 5.30
print(f"You can spend {dollar:.2f} dollars")