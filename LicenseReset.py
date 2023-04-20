from datetime import datetime, timedelta
import os
import grp


def licence(name, key):
    file = f"/usr/include/spammailer/licences/{name}.licence"
    gid = grp.getgrnam('spamusers').gr_gid
    try:
        index = 0
        max_index = len(key) - 1
        limit = input(f"enter daily limit for {name}:>>")
        xall = f"0,{limit},{datetime.today() - timedelta(3)}"
        data = bytes(xall, 'utf-8')
        try:
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
    except KeyError:
        print(f"user {name} or group spamusers not found")
        return


def createuser(name):
    password = f"keY-{name.capitalize()}TimePa$$"
    print(f"User {name} created successfully")
    licence(name, password)


createuser(str(input("Enter User name:>> ")))