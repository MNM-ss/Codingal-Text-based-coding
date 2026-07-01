# for srtings (sentences and symbols) we use inverted ocomma, they can never be with numbers as numbers are integers, we use them without the inverted comma and combine the integer with the string usually through a comma

#eg1
print("Welcome to the world of Coding!")
#eg2
print(4)

#for next line (like when you press enter on keyboard) use\n
print("Hello,\n My name is Manha!")

#Pass multiple ARGUMENTS for PRINTING. (use comma)
print("hello", 5)

#End argument with print Statement
print("Welcome to ", end="*")
# this doesn't work: print("Welcome to ", end=5)

# variablest

x = 5
y= "Manha"

print(x)
print(y)
print("x")

codingal ="codingal"
print(codingal)




import keyword

#Print all python keywords

print("Python keywords are...\n")
print(keyword.kwlist)





# User input
name = input("\nEnter your name please: ")

print("\nHello, ", name, "\nWelcome to Codingal!")
print("\nHello, ", name, "Welcome to Codingal!")