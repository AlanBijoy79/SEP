c_pass="123456"
for i in range(4):
    if i<3:
        password=input("Enter your password:")
        if password==c_pass:
            print("Access granted")
            break
        else:
            print("Access denied")
    else:
        print("No more attempts...please try again later")
    