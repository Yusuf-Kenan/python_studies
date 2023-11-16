users= [
    {"username":"admin", "email":"admin@email.com", "password":"1234"}
]
current_user= []

while True:
    print("USER APP".center(100))
    choice = input("1- Register \n2- Login \n3- Logout \n4- My Identity \n5- Exit \n\n- Your Choice: ")
    if choice == "5":
        break
    #Register
    elif choice == "1":
        r_email = input("email: ")
        r_username = input("username: ")
        r_password = input("password: ")
        new_user = {"username":r_username, "email":r_email, "password":r_password}
        users.append(new_user)
        current_user.append(new_user)
        print("Succesfully Registered")
    #Login    
    elif choice == "2":
        if len(current_user)==0:
            username = input("username: ")
            password = input("password: ")
            for user in users:
                if (username == user["username"] or username == user["email"]) and password == user["password"]:
                    print("Succesfully Loged In")
                    current_user.append(user)
                else:
                    print("username or password is wrong")
        else:
            print("You are already loged")
    #Logout
    elif choice == "3":
        if len(current_user) != 0:
            current_user.clear()
        else:
            print("Before logout you have to login")
    #My Identity
    elif choice == "4":
        if len(current_user) != 0:
            print(current_user)
        else:
            print("To see your identity you have to login")
    else:
        print("Wrong choice")
    print("*********************".center(100))
    