def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True
    return has_upper and has_lower and has_digit and has_special
print(is_valid_password("ValidP@ss1"))  
print(is_valid_password("weak"))  
