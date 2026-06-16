from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

def encrypt_file(filepath):

    with open(filepath, "rb") as file:
        data = file.read()

    encrypted = cipher.encrypt(data)

    new_file = filepath + ".enc"

    with open(new_file, "wb") as file:
        file.write(encrypted)

    return new_file