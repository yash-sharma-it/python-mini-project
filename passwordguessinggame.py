import random

easy_words = ["apple","fish","star","game","king","tree","book","cake"]
medium_words = ["planet","castle","monkey","guitar","window","garden","silver","camera"]
hard_words = ["dinosaur","medicine","umbrella","volcano","festival","adventure","internet","champion"]

print("WELCOME to the PASSWORD Guessing GAME")
print("Choose a difficuilty level: easy, medium or hard")

level = input("Enter Difficulty: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret  = random.choice(medium_words)
elif level == "hard":
    secret  = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret Word")

while True:
    guess = input("Enter your guess:  ").lower()
    attempts += 1

    if guess == secret:
        print(f"congratulations! You Guessed it Right in {attempts} attempts.")
        break
    
    hint = ""
#very difficult part 
    for i in range(len(secret)):
        if i < len(guess) and  guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("HINT : ", hint)
print("Game over")

