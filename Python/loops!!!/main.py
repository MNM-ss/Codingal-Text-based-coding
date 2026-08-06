#input an integer value

n = int(input("Enter the number whose sum you want to find: "))
sum=0
#Iterates for n+1 times: i=1 to n+1
for i in range(1, n+1):
    sum=sum+i
    print("\nSum =", sum)
print("\nSum =", sum)


#Input a word or sentence

string = input("Please enter your own String : ")

string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i + string2
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)


# input number greater than 1
n = int(input("Enter the value of n: "))

print ("numbers from {0} to {1} are: ".format(n,1))

# loop to print numbers
for i in range(n,0,-1):
    print(i)















    