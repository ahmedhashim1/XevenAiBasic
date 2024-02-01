passw = ""

while passw != "secret":
    passw = input("Enter password: ")
    if passw == "secret":
        print("Access granted")
    else:
        print("Invalid password")
