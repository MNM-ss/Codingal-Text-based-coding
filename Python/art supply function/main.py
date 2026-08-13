
def greet_customer():
    print("Welcome to the Art supply billing!")
    print("The best quality supplies in bd!")

greet_customer()

price_per_brush = float(input("Enter the price per brush in dollars: "))
brushes_sold = int(input("Enter the number of brushes sold: "))

def calculate_total(price, brushes):
    total = price * brushes
    return total

total_cost = calculate_total(price_per_brush, brushes_sold)

rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(brushes):
    if brushes >= 5:
        return "Big order! Thanks so much for your support!"
    else:
        return "Thanks for stopping by!"

closing_message = thank_you_message(brushes_sold)

print("")
print(" ==== Art SUPPLIES RECEIPT ====")
print("Price Per Brush:", price_per_brush)
print("Brushes Sold:", brushes_sold)
print("Total Cost:", rounded_total)
print("Amount Paid:", amount_paid)
print("Change Due:", rounded_change)
print(closing_message)
print("==================================")