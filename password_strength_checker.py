print("========= Password Strength Checker =========")
print("---------------------------------------------")

# List of common, weak passwords
common_passwords = ["password", "abc123", "password123", "123456", "123456789", "qwerty", "letmein", "admin", "welcome"]

# Function to evaluate password strength
def check_password_strength(password):
    score = 0
    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False

    if password.lower() in common_passwords:
        print("Warning: This is a very common password and easy to hack!")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        else:
            has_symbol = True

    if len(password) >= 8:
        score += 1
    else:
        print("Password should be at least 8 characters long.")

    if has_upper:
        score += 1
    else:
        print("Password should include at least one uppercase letter.")

    if has_lower:
        score += 1
    else:
        print("Password should include at least one lowercase letter.")

    if has_number:
        score += 1
    else:
        print("Password should include at least one numeric character.")

    if has_symbol:
        score += 1
    else:
        print("Password should include at least one special character.")

    if score <= 2:
        print("Password Strength: Weak")
    elif score <= 4:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")

while True:
    password = input("Enter a password (or type 'quit' to exit): ")

    if password.lower() == "quit":
        print("Program ended.")
        break

    check_password_strength(password)