from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password?")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

#key + password + text to encrypt = random text
#random text + key + password = text to encrypt

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_passw = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_passw)

            
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")
        
        
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit?").lower()
    
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
