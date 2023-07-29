try:
    name = input("enter your name = ")
    password = input("enter your password = ")
    if name == "admin" and password == "admin":
        print("you successfully logged in")
    else:
        raise Exception("wrong password")
except Exception as e:
    print(e)
