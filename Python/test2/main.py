def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Please type 1 for add, 2 for subtract, 3 for multiply, 4 for divide depending on the operation you want.")
choice = int(input("Choose operation (1/2/3/4): "))

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == 1:
        print("Result: ", add(num1, num2))
    elif choice == 2:
        print("Result: ", subtract(num1, num2))
    elif choice == 3:
        print("Result: ", multiply(num1, num2))
    elif choice == 4:
        print("Result: ", divide(num1, num2))
    else:
        print("Invalid, please try again")

except ValueError:
    print("Please give numbers only!!! Also please choose correct operation number.")

except ZeroDivisionError:
    print("You can not divide by zero, try again!")