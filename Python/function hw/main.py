def calculate_bill(food, drinks, tax, tip):
    subtotal = food + drinks
    tax_amount = subtotal * tax / 100
    tip_amount = subtotal * tip / 100
    total = subtotal + tax_amount + tip_amount
    return total


def seating_arrangements(people):
    if people == 0 or people == 1:
        return 1

    return people * seating_arrangements(people - 1)


food = 1200
drinks = 300
tax = 5
tip = 10

bill = calculate_bill(food, drinks, tax, tip)

print("Total Bill:", bill)
print("Document:")
print(seating_arrangements)

people = 4
arrangements = seating_arrangements(people)

print("Arrangements:", arrangements)

