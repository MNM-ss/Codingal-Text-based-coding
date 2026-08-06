
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (n): "))


result = 1
count = 0

while count < exponent:
    result = result * base
    count = count + 1  

print(f"{base} raised to the power of {exponent} is {result}")
