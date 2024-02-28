import getpass
import re

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

# Function to check if the email is valid
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

# Function for user signup
def signup():
    while True:
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")
        confirm_password = getpass.getpass("Confirm password: ")
        email = input("Enter your email: ")

        if is_valid_email(email) and password == confirm_password:
            print("Signup successful!")
            return username  # Return the username if signup is successful

        print("Your email and or password is incorrect. Please try again.")

    # Return a default value in case signup is not successful
        return "DefaultUsername"


# Function for guessing the number
def guess_the_number():
    import random
    secretNumber = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20.")

    for guessesTaken in range(1, 7):
        print("Take a guess.")
        guess = int(input())

        if guess < secretNumber:
            print("Your guess is too low. Try again.")
        elif guess > secretNumber:
            print("Your guess is too high. Try again.")
        else:
            break

    if guess == secretNumber:
        print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
    else:
        print("Incorrect. The number I was thinking of was " + str(secretNumber) + ".")

# Function for rock-paper-scissors game
def rock_paper_scissors():
    import random, sys

    print("ROCK, PAPER, SCISSORS")

    wins = 0
    losses = 0
    ties = 0

    while True:
        print(f""" 
{green} Wins: {end} {bold} {wins} {end} 
{red} Losses: {end} {bold} {losses} {end}
{blue} Ties: {end} {bold} {ties} {end}""")
        while True:
            print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
            playerMove = input()
            if playerMove == "q":
                sys.exit()
            if playerMove == "r" or playerMove == "p" or playerMove == "s":
                break
            print("Type one of r, p, s, or q.")

        if playerMove == "r":
            print("ROCK versus...")
        elif playerMove == "p":
            print("PAPER versus...")
        elif playerMove == "s":
            print("SCISSORS versus...")

        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = "r"
            print("ROCK")
        elif randomNumber == 2:
            computerMove = "p"
            print("PAPER")
        elif randomNumber == 3:
            computerMove = "s"
            print("SCISSORS")

        if playerMove == computerMove:
            print("It's a tie!")
            ties = ties + 1
        elif playerMove == "r" and computerMove == "s":
            print("You win!")
            wins = wins + 1
        elif playerMove == "p" and computerMove == "r":
            print("You win!")
            wins = wins + 1
        elif playerMove == "s" and computerMove == "p":
            print("You win!")
            wins = wins + 1
        elif playerMove == "r" and computerMove == "p":
            print("You lose!")
            losses = losses + 1
        elif playerMove == "p" and computerMove == "s":
            print("You lose!")
            losses = losses + 1
        elif playerMove == "s" and computerMove == "r":
            print("You lose!")
            losses = losses + 1

# Main part of the program
username = ""
answer = input(f"Would you like to {underline} 1. make an account {end} or {underline} 2. continue as a guest? {end}: ")

if answer.upper() == "2":
    print("Welcome Guest!")
elif answer.upper() == "1":
    username = signup()
    print("Welcome " + username + "!")

print("""What would you like to do? You can do:
1. Guess the number 
2. Rock paper scissors 
3. Quit""")
answer = input()

if answer == "1" or answer.upper() == "GUESS THE NUMBER":
    guess_the_number()
elif answer == "2" or answer.upper() == "ROCK PAPER SCISSORS":
    rock_paper_scissors()
elif answer == "3" or answer.upper() == "QUIT":
    print("Goodbye!")
