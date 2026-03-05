import random

# Setting the range between 20 and 40
secret_number = random.randint(20, 40)
guess = 0
tries = 0
lives = 5

print("------------------------------")
print("   STAY DOWN 5: THE GAME     ")
print("------------------------------")
print("I'm thinking of a number between 20 and 40.")
print("You only have 5 lives. Good luck!")
print("")

# The game runs as long as you have lives and haven't guessed right
while guess != secret_number and lives > 0:
    print("Lives remaining:", lives)
    
    user_input = input("Enter your guess: ")
    guess = int(user_input)
    
    # Update our counters
    tries = tries + 1
    lives = lives - 1
    
    if guess > secret_number:
        print("Too high! Try a smaller number.")
        print("")
    elif guess < secret_number:
        print("Too low! Try a bigger number.")
        print("")
    else:
        print("------------------------------")
        print("🎯 YOU GOT IT!")
        print(f"The number was {secret_number}!")
        print("Total tries:", tries)
        print("------------------------------")

# If they ran out of lives
if lives == 0 and guess != secret_number:
    print("GAME OVER!")
    print(f"You ran out of lives. The number was {secret_number}.")

print("")
print("Thanks for playing STAY DOWN 5!")

