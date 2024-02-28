import os
import sqlite3
import getpass
import re
import sys

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
def signup(connection):
    while True:
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")

        # Check if the password is not empty
        while not password:
            print("Password cannot be empty. Please try again.")
            password = getpass.getpass("Enter a password: ")

        confirm_password = getpass.getpass("Confirm password: ")

        # Check if the password and confirm password match
        while password != confirm_password:
            print("Passwords do not match. Please try again.")
            password = getpass.getpass("Enter a password: ")
            confirm_password = getpass.getpass("Confirm password: ")

        email = input("Enter your email: ")

        # Check if the email is valid
        while not is_valid_email(email):
            print("Invalid email. Please try again.")
            email = input("Enter your email: ")

        cursor = connection.cursor()

        # Check if the username or email already exists
        cursor.execute("SELECT * FROM users WHERE username=? OR email=?", (username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username or email already exists. Please choose a different one.")
        else:
            # Insert the new user into the database
            cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
            connection.commit()
            print("Signup successful!")
            view_all_accounts(connection)  # View all accounts after successful signup
            return username

# Function for user login
def login(connection):
    while True:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        cursor = connection.cursor()
        # Check if the username and password match an existing account
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        existing_user = cursor.fetchone()

        if existing_user:
            print(f"Login successful! Welcome back, {username}!")
            return username
        else:
            print("Invalid username or password. Please try again.")

# Function for viewing all accounts in the database
def view_all_accounts(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    accounts = cursor.fetchall()

    print("\nAll Accounts:")
    for account in accounts:
        print(account)

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
print(f"{red}{bold}{underline}If you are not running the program off of a computer owned by the code creator, the program will not work as the database is locally stored, not on a server.{end}")
answer = input(f"To continue with the program, {italics}enter '1'{end}. ")

if answer.upper() == "1":
    # Specify the path for the database file on the desktop
    db_path = "/home/runner/Desktop/MyDatabase/users.db"

    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
    except sqlite3.OperationalError as e:
        print(f"Error connecting to the database: {e}")
        sys.exit()
login_or_signup = input(f"Do you want to {underline}L{end}ogin or {underline}S{end}ignup? ").upper()

if login_or_signup == "L":
        username = login(connection)
elif login_or_signup == "S":
        username = signup(connection)
        print(f"Welcome {username}!")

print("""What would you like to do? You can do:
    1. Guess the number 
    2. Rock paper scissors 
    3. View all accounts
    4. Quit""")
answer = input()

if answer == "1" or answer.upper() == "GUESS THE NUMBER":
        guess_the_number()
elif answer == "2" or answer.upper() == "ROCK PAPER SCISSORS":
        rock_paper_scissors()
elif answer == "3" or answer.upper() == "VIEW ALL ACCOUNTS":
        view_all_accounts(connection)
elif answer == "4" or answer.upper() == "QUIT":
        print("Goodbye!")
