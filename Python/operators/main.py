# ---Assignment Operator (=)---

# store the harvest in kg from each of the 5 fields
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110


# --- Arithmetic Operators (+, -, ", /)---
# calculate total and average harvest

total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest: ", total, "kg.")
print("Average per feild: ", average, "kg.")

#price per kg is 15 rupees - calculate total earnings

price_per_kg = 15
earnings = total * 15

print("Total earnings is : Rs. ", earnings, "$")

#floor division and modulus
#pack the harvest into bags, 25kg each

bags = total // 25
leftover = total % 25

print("Full bags packed:  ", bags)
print("leftovers:  ", leftover)



# comparision operators
#comparing harvest from this year to last year

last_year = 500

print("Better than last year! : ", total > last_year )
print("Same as last year: ", total == last_year )
print("Poorer than last year... : ", total < last_year )

#Assignment Operators 

# A bonus field aids 30 kg to the total
total += 30
print("After bonus crop :", total, "kg")
# Subtract 15 kg saved as seeds for next season
total -=15
print("After seed reserve", total, "kg")




