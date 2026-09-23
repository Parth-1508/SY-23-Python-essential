def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for uppercase and lowercase letters
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    
    # Check for at least one digit
    has_digit = any(c.isdigit() for c in password)
    
    # All criteria must be met
    if has_upper and has_lower and has_digit:
        return True
    return False

print("Enter passwords to check (or type 'stop' to exit):")

while True:
    password = input("Enter password: ")
    
    # Check for exit command
    if password == "stop":
        print("Exiting password checker.")
        break
    
    # Check strength
    if check_password_strength(password):
        print("Result: Strong password\n")
    else:
        print("Result: Weak password\n")