# this release may have many bugs, but i will fix them in the next release.
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

def toDoList():
  tasks = []

  def addTask():
      task = input("Please enter a task to complete: ")
      tasks.append(task)
      print(f"Task '{task}' has been added to the list")

  def listTasks():
      if not tasks:
          print("There are currently no tasks.")
      else:
          print("Current Tasks: ")
          for index, task in enumerate(tasks):
              print(f"Task #{index}. {task}")

  def deleteTask():
      listTasks()
      try:
          taskToDelete = int(input("Enter the # of the task to delete: "))
          if taskToDelete >= 0 and taskToDelete < len(tasks):
              tasks.pop(taskToDelete)
              print(f"Task {taskToDelete} was deleted.")
          else:
              print(f"Task #{taskToDelete} was not found.")
      except:
          print("Invalid input.")

  if __name__ == "__main__":
      print("Welcome to the to-do list app!")
      while True:
          print("\n")
          print("Please select one of the following options.")
          print("-------------------------------------------")
          print("1. Add a new task")
          print("2. Delete a task")
          print("3. List current tasks")
          print("4. Quit")

          choice = input("Enter your choice: ")

          if(choice == "1"):
              addTask()
          elif (choice == "2"):
              deleteTask()
          elif (choice == "3"):
              listTasks()
          elif (choice == "4"):
             break
            
          else:
              print("Invalid input. Please try again.")

      print("Goodbye!")

def Calculators():
  whichCalc = input("Which calculator would you like to use? (1) Weight Calculator (2) Area Calculator")
  if whichCalc == "1":
    weightCalc()
  elif whichCalc == "2":
    areaCalc()

def areaCalc():
  width = float(input("Please enter the width of the rectangle: "))
  height = float(input("Please enter the height of the rectangle: "))
  print("The area of your rectangle is: " + str(width * height))
  print("The perimeter of your rectangle is: " + str(width + height))

def weightCalc():
  weight = float(input("Enter a weight: "))
  unit = input("Is this in (K)g or (L)bs: ")
  if unit.upper() == "K":
      converted = weight / 0.45
      print("Weight in Lbs:" + str(converted))
  else:
      converted = weight * 0.45
      print("Weight in Kgs: " + str(converted))

# Main part of the program
def main():
  username = ""
print(f"{red}{bold}{underline}If you are running the program off of a computer not owned by the code creator/owner, the program will not work as the database is locally stored, not on a server.{end}")
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

if login_or_signup == "L" or login_or_signup == "LOGIN":
        username = login(connection)
elif login_or_signup == "S" or login_or_signup == "SIGNUP":
        username = signup(connection)
        print(f"Welcome {username}!")

print("""What would you like to do? You can do:
1. Guess the number 
2. Rock paper scissors
3. To-do list
4. View all accounts
5. Quit""")
answer = input()

if answer == "1" or answer.upper() == "GUESS THE NUMBER":
  guess_the_number()
elif answer == "2" or answer.upper() == "ROCK PAPER SCISSORS":
  rock_paper_scissors()
elif answer == "3" or answer.upper() == "TO-DO LIST":
  toDoList()
elif answer == "4" or answer.upper() == "VIEW ALL ACCOUNTS":
  view_all_accounts(connection)
elif answer == "5" or answer.upper() == "QUIT":
  print("Goodbye!")
elif answer == "6" or answer.upper() == "CALCULATORS":
  Calculators()

main()
