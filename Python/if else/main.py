num = 5
if num > 0:
    print(num, " is a positive integer")

num = 0
if num == 0:
    print(num, "is equal to zero.")

num = -6
if num < 0:
    print(num, "is a negative integer.")





cost_price = float(input("Please Enter the Actual Product price: "))
sale_price = float(input("Please Enter the Product Sale price: "))

if sale_price > cost_price:
 profit = sale_price - cost_price
 print("Total profit is  = {0}".format(profit))
else:
  loss = cost_price - sale_price
  print("Total loss is  = {0}".format(loss))