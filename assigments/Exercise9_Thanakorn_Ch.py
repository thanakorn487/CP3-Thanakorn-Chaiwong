UsernameInput = input("Username : ")
PasswordInput = input("Password : ")
while UsernameInput != "admin" or PasswordInput != "1234":
    print("Incorrect Username or Password!")
    print("Please, try again!")
    UsernameInput = input("Username : ")
    PasswordInput = input("Password : ")
print("Done!")