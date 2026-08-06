

rows = int(input("Please Enter the total Number of Rows"))
number = 1 #initialise by 1
print("Floyd's Triangle")
#outer loop for number of rows
for i in range(1, rows + 1):
        for j in range(1, i + 1):
         #display resuit
            print(number, end = " ")
            number = number + 1
        print()



n = 3
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(i):
        print(i, end=" ")
    print()


for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(i):
        print(i, end=" ")
    print()



    n = 3  

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
        
    for k in range((2 * i) - 1):
        print(k + 1, end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
        
    for k in range((2 * i) - 1):
        print(k + 1, end="")
    print()



