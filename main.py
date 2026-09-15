import random
import string

def make_password():
    print("Password Generator")
    
    length = int(input("How long should the password be? (min 8): "))
    if length < 8:
        print("Password too short. Must be 8 characters or more.")
        length=8
        
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers (0-9)? (y/n): ").lower() == 'y'
    use_symbols = input("Include special symbols (!@#$%^&*)? (y/n): ").lower() == 'y'

    if not (use_upper or use_lower or use_digits or use_symbols):
        print("You must pick at least one character type. Defaulting to lowercase.")
        use_lower = True

    all_characters = string.ascii_letters + string.digits + string.punctuation
     
    password = "".join(random.sample(all_characters, length)).replace(" ", "")
    
    print("Your Password: ", password)

make_password()
