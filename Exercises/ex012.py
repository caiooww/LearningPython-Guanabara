#* Create an algorithm that reads the price of a product and shows its new price, with a 5% discount.

price = float(input("Enter the price of the product: "))

newPrice = price * 0.95

print("The new price with a 5% discount is: $ {:.2f}".format(newPrice))