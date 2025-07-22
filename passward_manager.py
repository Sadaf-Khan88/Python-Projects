
from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("Key.Key" , "rb")
    key = file.read()
    file.close()
    return

master_pwd = input("What is the master passward? ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passward.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User : ",user, "|  Passward : ", fer.decrypt(passw.encode()).decode())
            

def add():
    name = input ("Enter the name : ")
    pwd = input("Enter the passward : ")

    with open("passward.txt", "a") as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")
       

while True:
    mode = input("Would you like to add new passward or view the existing once (add / view) or type q to quit : ").lower()

    if mode == "q":
        break

    if mode == "add":
        add()
        
    elif mode == "view":
        view()
        
    else:
        print("Not  avalid option")
        continue



