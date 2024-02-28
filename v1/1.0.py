import getpass

def signup():
    while True:
      username = input("Enter a username: ")
      password = getpass.getpass("Enter a password: ")
      confirm_password = getpass.getpass("Confirm password: ")
      email = input("Enter your email: ")
      if password == confirm_password:
        print("Signup successful!")
        break
      elif password != confirm_password:
        print("Your passwords do not match. Please try again.")

def login():
  login_username = input("Enter your username: ")
  login_password = getpass.getpass("Enter your password: ")
  print("Login successful!")

answer = input("Do you have an account? (yes/no): ")
if answer.upper() == "YES":
  login()
elif answer.upper() == "NO":
  signup()
