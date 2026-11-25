import random
play_again = "yes"

while play_again == "yes":

    number = random.randint(1, 100)
    attempts = 0

    guess = int(input("Enter your number: "))
    attempts += 1

    while guess != number:

        if guess > number:
            print("Too High!")

        elif guess < number:
            print("Too Low!")

        try:
            guess = int(input("Guess again: "))
            attempts += 1

        except ValueError:
            print("Please enter a valid number!")

    print("Congrats! You guessed it.")
    print("Total attempts:", attempts)

    play_again = input("Play again? yes/no: ").lower()

print("Thanks for playing!")
