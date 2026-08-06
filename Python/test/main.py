
secret = 27
attempts = 5

print("Guess a number between 1 and 50. Guess it in 5 tries!")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    
    if guess == secret:
        print("Congratulations! You guessed the secret number!")
        attempts = 0 
        
    else:
        attempts = attempts - 1
        
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess
            
        if diff >= 20:
            print("Hint: 🧊 ice cold")
        elif diff >= 10:
            print("Hint: 🥶 cold")
        elif diff >= 5:
            print("Hint: 🌡️ warm")
        else:
            print("Hint: 🔥 hot")
            
        if attempts > 0:
            print("Remaining lives:")
            for h in range(attempts):
                print("❤️")

if guess != secret:
    print("Game Over- The secret number was:")
    print(secret)
