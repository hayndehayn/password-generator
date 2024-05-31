import random
import string
import clipboard

length = int(input("Input password length: "))

def generate_password(length):
    global password
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")

def copy_to_clipboard():
    clipboard.copy(password)
    print("Password copied successfully!")

generate_password(length)
copy_to_clipboard()
