print("Input the quantity of widgets")
quantity = int(input())
price = 0
if quantity > 10000:
  price = 10
elif quantity >= 5000:
  price = 20
elif quantity < 5000:
  price = 30
extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax
print("Extended price: ", extended_price)
print("Tax: ", tax)
print("Total: ", total)