# Guess the number?

import random  

print("\tWelcome in the game: 'Guess the number'!")
print("\nI think about a number from 0 to 100.")
print("Try to guess it in as few attempts as possible.\n")

# set initial values
the_number = random.randint(1, 100)
guess = int(input("The number is: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("To large...")
    else:
        print("To small...")
            
    guess = int(input("The number is: "))
    tries += 1

print("You guessed it! The number is: ", the_number)
print("To guess it you needed", tries, "attempts!\n")
  
input("\n\nTo close the game, use Enter.")
