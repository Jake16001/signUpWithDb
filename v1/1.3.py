import getpass
import re

def is_valid_email(email):
      pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
      return re.match(pattern, email)

def signup():
      while True:
          username = input("Enter a username: ")
          password = getpass.getpass("Enter a password: ")
          confirm_password = getpass.getpass("Confirm password: ")
          email = input("Enter your email: ")
          if is_valid_email(email):
              if password == confirm_password:
                  print("Signup successful!")
                  break
          while True: 
            if password != confirm_password or not is_valid_email(email):
              print("Your email and or password is incorrect. Please try again.")
              password = getpass.getpass("Enter a password: ")
              confirm_password = getpass.getpass("Confirm password: ")
              email = input("Enter your email: ")
              if is_valid_email(email) and password == confirm_password:
                      print("Signup successful!")
            break
          break

                  
def login():
      login_username = input("Enter your username: ")
      login_password = getpass.getpass("Enter your password: ")
      print("Login successful!")

answer = input("Do you have an account? (yes/no): ")
if answer.upper() == "YES":
      login()
elif answer.upper() == "NO":
      signup()
