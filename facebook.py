user=input("enter the user")
password=int(input("enter the password"))
if user=="priyanka":
    if password==1234:
        print("welcome")
    elif user!="shital" and password==1234:
        print("the user is wrong")
    elif user=="priyanka" and password!=2345:
        print("the password is wrong")
else:
    print("create new account")
    user=input("enter the user")
    password=int(input("enter the password"))
    if user=="mamta":
        if password==4567:
            print("your account has been created")
        else:
            print("your account has not been created")
        