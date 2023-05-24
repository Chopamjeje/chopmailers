import time
from datetime import datetime, timedelta
import os
import pwd
import grp
import subprocess
import bcrypt
import crypt
import socket



def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def licence(name, key):
    try:
        pwd.getpwnam(name)
        gid = grp.getgrnam('spamusers').gr_gid
        subprocess.run(["usermod", "-aG", "spamusers", name])
    except KeyError:
        print(f"user {name} or group spamusers not found")
        return
    else:
        file = f"{os.path.dirname(os.path.realpath(__file__))}/licences/{name}.licence"
        index = 0
        max_index = len(key) - 1
        limit = input(f"enter daily limit for {name}:>>")
        xall = f"0,{limit},{datetime.today() - timedelta(3)}"
        data = bytes(xall, 'utf-8')
        try:
            os.makedirs(f"/home/{name}/attach", 0o777, exist_ok=True)
            with open(f"/home/{name}/fm.txt", 'w') as f:
                f.write("<p> Hello Word </p>")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(f"/home/{name}/leads.txt", 'w') as f:
                f.write("example-email@163.com, Name, Company Name\nexample2@gmail.com, Name Example, 2nd Company Name")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(f"/home/{name}/domains.txt", 'w') as f:
                f.write("giwindustries.com")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(f"/home/{name}/links.txt", 'w') as f:
                f.write("google.com, 2ndlink-if-any.com, 3rdlink-and-so-on.com.cn")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(f"/home/{name}/checks.txt", 'w') as f:
                f.write("test@test.me")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(f"/home/{name}/smtp.txt", 'w') as f:
                f.write("smtp.test.com|test@test.com|Passwd$$|465")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(file, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
        except Exception as ex:
            print(f"last error >> {ex}")
        else:
            print(f"Licence created successfully for {name}")
        print(f"User {name} created successfully\n=======================\nHost/Server: {get_ip_address()}\nUsername: {name}\nPassword: {key}\n=======================\n")


def createuser(name):
    password = f"keY-{name.capitalize()}TimePa$$"
    encPass = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))
    subprocess.run(["useradd", "-p", encPass, name])
    licence(name, password)


def check_password(password):
    hashed_password = bcrypt.hashpw(b'keY[0]Pass', bcrypt.gensalt())
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False


def check_group_create():
    try:
        grp.getgrnam('spamusers')
        #print("Group 'spamusers' already exists.")
    except KeyError:
        os.system("groupadd spamusers")
        #print("Group 'spamusers' created.")


while True:
    os.system('clear')
    pxm = input("Enter admin password to create user ::>")
    if check_password(pxm):
        check_group_create()
        name = input("Enter username to be created ::>")
        try:
            createuser(str(name))
        except Exception as ex:
            print(f" error creating user >> {ex}")
            time.sleep(1)
            continue
        else:
            break
    else:
        print("Incorrect Password")
