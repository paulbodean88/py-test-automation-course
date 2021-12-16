"""
1. get the user,pwd and current sold from the console
2. validate the user and password
3. Enable the login through an enter
4. Display the sold after the login
5. Retrieve an amount of cash
6. Display the password encrypted e.g. instead of 'abcd' show '****'.
7. Be aware that the nr of '*' should be equal with the length of the pwd

"""

# Define the expected results in terms of code
expected_usr: str = "Paul"
expected_pwd: str = "abcg"
expected_sold: int = 10000

# Implement the test case
usr = input("Please enter a valid username ")
assert usr == expected_usr
pwd = input("Please enter a valid password ")
assert pwd == expected_pwd
input("Press enter to login")
print(f"Logged in successfully, your sold is {expected_sold}")

cash = int(input("How much cash do you want?"))
print(f"Your sold now is {expected_sold - cash} RON")

show_pwd = len(pwd)
print(f'The password for user {usr} is {show_pwd * "*"}, is {show_pwd} characters long', end='')
print(f'The password for user {usr} is {show_pwd * "*"}, is {show_pwd} characters long')
