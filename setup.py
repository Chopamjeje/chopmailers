#yum install wget
#wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
#python get-pip.py
#pip install requests


import os
import zipfile
import shutil
import requests
import os
import sys
import subprocess


def install_python_and_upgrade_pip():
    subprocess.call("yum update -y", shell=True)
    subprocess.call("yum install openssl-devel bzip2-devel libffi-devel -y", shell=True)
    subprocess.call("yum groupinstall 'Development Tools' -y", shell=True)
    subprocess.call("yum install wget -y", shell=True)
    subprocess.call("wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz", shell=True)
    subprocess.call("tar -xzf Python-3.10.2.tgz", shell=True)
    os.chdir("Python-3.10.2")
    subprocess.call("./configure --enable-optimizations", shell=True)
    subprocess.call("make altinstall", shell=True)
    subprocess.call("python3.10 -V", shell=True)
    subprocess.call(["python3", "-m", "pip", "install", "--upgrade", "pip"])


def move_files(dst_dir):
    files = ['mailer.py', 'constructed.py', 'bigVar.py', 'CreateUser.py', 'functions.py', 'DeleteUser.py', 'LicenseReset.py']
    # Move each file to the destination directory
    for file in files:
        dst_file = os.path.join(dst_dir, file)
        os.rename(file, dst_file)



def install_wget_pip_git():
    # Install wget
    subprocess.call(['sudo', 'yum', 'install', 'wget'])
    
    # Download get-pip.py using wget
    subprocess.call(['wget', 'https://bootstrap.pypa.io/pip/2.7/get-pip.py'])
    
    # Install pip using python
    subprocess.call(['sudo', 'python', 'get-pip.py'])
    
    # Install git
    subprocess.call(["yum", "install", "git", "-y"])

install_wget_pip_git()

# Create folders
folder_list = [
    '/usr/include/spammailer',
    '/usr/include/spammailer/images',
    '/usr/include/spammailer/attached',
    '/usr/include/spammailer/leads',
    '/usr/include/spammailer/licences',
]

for folder in folder_list:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(folder+"created successfully")

# Create files
file_list = [
    '/usr/bin/spam',
    '/usr/bin/spamdel',
    '/usr/bin/spamlic',
    '/usr/bin/spamuser',
    # '/usr/include/pxmailer/latest.py',
    # '/usr/include/pxmailer/constructed.py',
    # '/usr/include/pxmailer/functions.py',
    # '/usr/include/pxmailer/bigVar.py',
    # '/usr/include/pxmailer/CreateUser.py',
]

for file in file_list:
    open(file, 'a').close()


def clone_and_extract_repo(github_link):
    os.system('git clone '+github_link)
    repo_name = github_link.split('/')[-1].replace('.git', '')
    zip_file_path = repo_name+".zip"
    
    response = requests.get('https://github.com/'+github_link+'/archive/refs/heads/main.zip')
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)
    os.remove(zip_file_path)

    os.chdir(repo_name)
    return os.getcwd()


try:
    finalpath = clone_and_extract_repo("https://github.com/Chopamjeje/chopmailers.git")
except Exception as e:
    print("error check"+str(e))
else:
    move_files('/usr/include/spammailer/')

# get_private_github_repo('https://github.com/Chopamjeje/chopmailers.git', '/usr/include/pxmailer/')

# Give permissions to folders
folder_permissions = [
    '/usr/include/spammailer/attached',
    '/usr/include/spammailer/leads',
    '/usr/include/spammailer/licences',
]

for folder in folder_permissions:
    os.chmod(folder, 0o777)

# Give permissions to files
file_permissions = [
    '/usr/include/spammailer/bigVar.py',
    '/usr/include/spammailer/functions.py',
    '/usr/include/spammailer/CreateUser.py',
    '/usr/include/spammailer/constructed.py',
    '/usr/include/spammailer/latest.py',
    '/usr/include/spammailer/DeleteUser.py',
    '/usr/include/spammailer/LicenseReset.py',
    '/usr/bin/spamuser',
    '/usr/bin/spamdel',
    '/usr/bin/spamlic',
    '/usr/bin/spam',
]

for file in file_permissions:
    os.chmod(file, 0o777)

# Install required packages
subprocess.call(["yum", "update", "-y"])
subprocess.call(["yum", "install", "-y", "python3"])
subprocess.call(["sudo", "yum", "install", "epel-release", "-y"])
subprocess.call(["sudo", "yum", "install", "python-pip", "-y"])
subprocess.call(["yum", "install", "git", "-y"])
subprocess.call(["git", "clone", "https://github.com/reingart/pyfpdf.git"])
os.chdir("pyfpdf")
subprocess.call(["python", "setup.py", "install"])
subprocess.call(["pip", "install", "fpdf"])
subprocess.call(["yum", "install", "dos2unix"])

# Perform dos2unix on specified files
dos2unix_list = [
    '/usr/include/spammailer/latest.py',
    '/usr/include/spammailer/constructed.py',
    '/usr/include/spammailer/bigVar.py',
    '/usr/include/spammailer/CreateUser.py',
    '/usr/include/spammailer/functions.py',
    '/usr/include/spammailer/DeleteUser.py',
    '/usr/include/spammailer/LicenseReset.py',
    '/usr/bin/spam',
    '/usr/bin/spamlic',
    '/usr/bin/spamdel',
    '/usr/bin/spamuser',
]

for file in dos2unix_list:
    subprocess.call(["dos2unix", file])

# Write content to /usr/bin/pxmailer
with open("/usr/bin/spam", "w") as f:
    f.write("#!/bin/bash\npython3 /usr/include/spammailer/latest.py")


# Make /usr/bin/pxmailer file executable
os.chmod("/usr/bin/spam", 0o777)

# Write content to /usr/bin/pxmailer
with open("/usr/bin/spamlic", "w") as f:
    f.write("#!/bin/bash\npython3 /usr/include/spammailer/LicenseReset.py")


# Make /usr/bin/pxmailer file executable
os.chmod("/usr/bin/spamlic", 0o777)

# Write content to /usr/bin/pxuser
with open("/usr/bin/spamuser", "w") as f:
    f.write("#!/bin/bash\npython3 /usr/include/spammailer/CreateUser.py")

# Make /usr/bin/pxuser file executable
os.chmod("/usr/bin/spamuser", 0o777)

# Write content to /usr/bin/pxuser
with open("/usr/bin/spamdel", "w") as f:
    f.write("#!/bin/bash\npython3 /usr/include/spammailer/DeleteUser.py")

# Make /usr/bin/pxuser file executable
os.chmod("/usr/bin/spamdel", 0o777)

# Convert files to Unix line endings

subprocess.call(["dos2unix", "/usr/include/spammailer/latest.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/constructed.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/bigVar.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/CreateUser.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/functions.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/CreateUser.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/DeleteUser.py"])
subprocess.call(["dos2unix", "/usr/bin/spam"])
subprocess.call(["dos2unix", "/usr/bin/spamuser"])
subprocess.call(["dos2unix", "/usr/bin/spamlic"])
subprocess.call(["dos2unix", "/usr/bin/spamdel"])

# Install python3
if sys.version_info[0] < 3:
    subprocess.call(["yum", "update", "-y"])
    subprocess.call(["yum", "install", "-y", "python3"])

# Install pip
subprocess.call(["sudo", "yum", "install", "epel-release"])
subprocess.call(["sudo", "yum", "install", "python-pip"])


# Install fpdf
subprocess.call(["git", "clone", "https://github.com/reingart/pyfpdf.git"])
os.chdir("pyfpdf")
subprocess.call(["python", "setup.py", "install"])
subprocess.call(["python3", "setup.py", "install"])
subprocess.call(["pip", "install", "fpdf"])
subprocess.call(["pip3", "install", "fpdf"])

# Install dos2unix
subprocess.call(["yum", "install", "dos2unix"])
subprocess.call(["dos2unix", "/usr/include/spammailer/latest.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/constructed.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/bigVar.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/CreateUser.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/functions.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/DeleteUser.py"])
subprocess.call(["dos2unix", "/usr/include/spammailer/CreateUser.py"])
subprocess.call(["dos2unix", "/usr/bin/spam"])
subprocess.call(["dos2unix", "/usr/bin/spamuser"])
subprocess.call(["dos2unix", "/usr/bin/spamlic"])
subprocess.call(["dos2unix", "/usr/bin/spamdel"])
install_python_and_upgrade_pip()
subprocess.call(["pip3", "install", "bcrypt"])
#os.remove(finalpath)
shutil.rmtree(finalpath)
print("DONE")
