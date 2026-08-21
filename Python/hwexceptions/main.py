
try:
        fee = int(input("Enter your total fee: "))
        dis_per = int(input("Enter the discount percentage (without a percentage sign): "))

        discount = fee*(dis_per/100)
        discount_fee = fee-discount

        print(f"Your Discount is {discount}$ and your New total is {discount_fee}$!")
        

except ValueError:
     print("Please enter a INTEGER, not any letter or symbols!")
