# Caleb Behrman
# UWYO COSC 1010
# 11/20/24
# Lab 10
# Lab Section: 15

from hashlib import sha256
from pathlib import Path

def get_hash(to_hash):
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()
    #this just generates the sh256 thing for this string

def crack_password():
    try:
        #this reads the hash from the hash file
        with open('hash', 'r') as hash_file:
            target_hash=hash_file.read().strip() #reads it
    except Exception as e:
        print(f"Error reading hash file: {e}")
        return

    try:
        #reads the password from the rockyou file
        with open('rockyou.txt', 'r') as rockyou_file:
            for password in rockyou_file:
                password=password.strip()
                hashed_password=get_hash(password)  #this hashes the passswrod
                
                if hashed_password==target_hash:
                    print(f"Password found: {password}")
                    return  #this stops the looop once the password is foudn
    except Exception as e:
        print(f"Error reading rockyou.txt: {e}")
        return

    print("Password not found in the list.")
crack_password()