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



  i = int(input("Please enter a number: "))
  if i < 15:
     print("Your number is smaller than 15")
     print("The string you are reading is in IF block")
  else:
    print("Your Number is greater than 15")
    print("The string you are reading is in ELSE block in IF")

    print("Meanwhile The string you are reading now is in no block. Not in if, or else")
    


number = int(input("Please input a number to check wether it is even or odd. : "))

if number%2 == 0:
   print(number, " is an even number.")
else:
   print(number, " is an odd number.")

if number%2==0:
   print(number, " is an even number.")
else:
   print(number, " is an odd number.")

if number%2==0 :
   print(number, " is an even number.")
else:
   print(number, " is an odd number.")

if number %2==0:
   print(number, " is an even number.")
else:
   print(number, " is an odd number.")

if number %2 == 0:
   print(number, " is an even number.")
else:
   print(number, " is an odd number.")