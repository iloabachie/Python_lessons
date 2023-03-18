from hashlib import pbkdf2_hmac
import os

password = input("Password: ")


def hashPassword(password):
    salt = os.urandom(32)      
    key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    if __name__ == '__main__':
        print(salt)
        print(key.hex())
        print(key)
        

hashPassword(password)
