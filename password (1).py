password = input("Enter your password: ")
has_upper = False
has_lower = False
has_digit = False
if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    if has_upper and has_lower and has_digit:
        print("Password is strong")
    else:
        print("Password is weak")
else:
    print("Password is weak")
