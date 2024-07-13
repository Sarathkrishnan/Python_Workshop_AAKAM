usernames = "akshara"
password = "coolpython098"

user_name = input("Enter you user name:")
user_pass = input("Enter your password:")

"""
write if conditon to verify the user name and password
"""

if user_name == usernames:
    if user_pass == password:
        print("Login sucess")
else:
    print("Invalid user name. Try again")
