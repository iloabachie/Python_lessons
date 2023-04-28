from hashlib import pbkdf2_hmac
import os


def hashPassword():
    password = input("Password: ")
    salt = os.urandom(32)      
    key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    if __name__ == '__main__':
        print(salt)
        print(key.hex())
        print(key)
    
    return key
        

if __name__ == '__main__':
    print('function', hashPassword())
