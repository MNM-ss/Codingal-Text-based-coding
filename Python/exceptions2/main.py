try:
    num1, num2 = eval(input("Please enter two numbers in order of division, seperated by a comma: "))
    result = num1/num2
    print("The Result of the division of your numbers are: ", result)

except ZeroDivisionError:
    print("No division by zero please!")
except SyntaxError  :
    print("Please Enter comma! like 1, 2")
except:
    print("wrong input!")
else:
    print("No exeptions")
finally:
    print("THis will execute")

valid = False
while not valid: 
    try:
        n=int(input("Enter a number: "))
        while n%2==0:
            print("bye")
        valid = True

    except ValueError:
        print("Invalid")