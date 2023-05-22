# !/usr/bin/python
# coding=utf-8

# imports
# from bigVar import *
from functions import *
from constructed import PDF
import random
# from threading import Thread
# from queue import Queue
import smtplib#, ssl
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import os
from pathlib import Path
from email.mime.base import MIMEBase
from email import encoders
import getpass
from time import sleep as tsleep
from datetime import datetime

check()
os.system('clear')
defsub = ""
successcount = ""
mex = ""

sendmode = int(input("Would you like to use smtp or localhost?\n1. SMTP\n2. Localhost\n:>> "))

if sendmode == 2:
    mex = str(input("Enter your reply to mail:>> "))

sub = int(input(
    "What type of message do you want to send\n1. linkedin \n2. purcahse order \n3. payment \n4. quota \n5. big file. \n6. enter your subject. \n ::> "))

if sub == 6:
    defsub = str(input("Enter Your Subject \n ::> "))

get_domain()

def mailer(x, y, z):
    successcount = 0
    check()
    email, vname, vcorp = x, y, z
    # amount = f"{phone(2)},{phone(3)}.{phone(2)}"
    pdate = str(datetime.today()).split(" ")[0]
    vdate = str(datetime.today() - timedelta(2)).split(" ")[0]
    name = namegen()
    subj = subjectgen(sub)
    corp = company()
    submessage = submsg()
    footer = footers()
    subordermsg = subordermsgs()
    greeting = greetings()
    location = country()
    location1 = country()
    location2 = country()
    location3 = country()
    codex = base64enc(email)
    link = str(getlinks(email))

    pirand = str(randomString(random.randrange(2, 13)))

    domain = random.choice(domainlist)
    firstname = f"{name.split(' ')[0]}"
    lastname = f"{name.split(' ')[1]}"
    fullname = f"{firstname} {lastname}"
    cell = f"+{randint(random.randrange(2, 3))} ({randint(3)}) - {randint(7)}"
    fullemail = f"{lastname}_{firstname}.{randomchar(random.randrange(2, 8))}@{domain}"
    ccname = str(namegen())
    ccemail = f'{ccname.split(" ")[1]}.{ccname.split(" ")[0]}{domain}'
    cc = f'"{ccname}"({ccemail})'
    position = str(posgen())
    mex = "infobuyingsales@naver.com"
    me = f'"{fullname}"<{fullemail.lower()}>'
    userdomain = email.split('@')[1]
    userdomainfront = userdomain.split('.')[0]
    emailuser = email.split('@')[0]
    if sendmode == 1:
        smtp_settings = random.choice(read_smtp_file())
        smtpuser = smtp_settings["smtpuser"]
        smtp_pass = smtp_settings["smtppass"]
        smtp_server = smtp_settings["smtpserver"]
        port = smtp_settings["smtpport"]
        me = f'"{fullname}"<{smtpuser}>'
        mex = f"{smtpuser}"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"{subj}"
    msg['From'] = me
    msg['To'] = email
    msg.add_header('reply-to', mex)

    text = f"see below information \n\n{link}\n\nThanks awaitng your quick action"  # text
    replaceable = {
        '{email}': f'{email}',
        '{domain}': f'{domain}',
        '{name}': f'{name}',
        '{cc}': f'{str(cc).lower()}',
        '{ccname}': f'{ccname}',
        '{ccemail}': f'{ccemail.lower()}',
        '{me}': f'{me}',
        '{emailuser}': f'{emailuser}',
        '{userdomain}': f'{userdomain}',
        '{link}': f'{link}',
        '{position}': f'{position}',
        '{userdomainfront}': f'{userdomainfront}',
        '{subj}': f'{subj}',
        '{fullemail}': f'{fullemail}',
        '{fullemail.lower()}': f'{fullemail.lower()}',
        '{corp}': f'{corp}',
        '{mex}': f'{mex}',
        '{submessage}': f'{submessage}',
        '{firstname}': f'{firstname}',
        '{lastname}': f'{lastname}',
        '{fullname}': f'{fullname}',
        '{greeting}': f'{greeting}',
        '{subordermsg}': f'{subordermsg}',
        '{footer}': f'{footer}',
        '{location}': f'{location}',
        '{location1}': f'{location1}',
        '{location2}': f'{location2}',
        '{location3}': f'{location3}',
        '{cell}': f'{cell}',
        '{codex}': f'{codex}',
        '{vname}': f'{vname}',
        '{vcorp}': f'{vcorp}',
        '{vdate}': f'{vdate}',
        '{pdate}': f'{pdate}',
        '{pxrand}': f'<font id="{pirand}">{randomchar(random.randrange(2, 13))}&shy;{datetime.today()}</font>',
        '{pirand}': f'{pirand}'
    }

    fmname = f"{str(Path.home())}/fm.txt"
    with open(f'{fmname}', 'r') as f:
        html = f.read()
        for key, value in replaceable.items():
            html = html.replace(key, value)
        html = replace_placeholders(html)
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    try:
        attfile = ""
        if attach == "1":
            ext = ('.txt',
                   '.html',
                   '.shtml',)
            try:
                if str(f".{filename.split('.')[1]}") in ext:
                    with open(f'{str(filename)}', 'r') as z:
                        dits = f"{z.read()}"
                        for key, value in replaceable.items():
                            dits = dits.replace(key, value)
                        dits = replace_placeholders(dits)
                    attfile = f'{str(Path.home())}/attach/{str(filename)}'
                    with open(f'{attfile}', 'w') as x:
                        x.write(dits)
            except Exception as eg:
                print(eg)
                pass
            else:
                attachment = open(attfile, 'rb')
                part3 = MIMEBase('application', 'octet-stream')
                part3.set_payload((attachment).read())
                encoders.encode_base64(part3)
                attachname = os.path.basename(str(filename))
                part3.add_header('Content-Disposition', 'attachment; filename="%s" ' % attachname)
                msg.attach(part3)
        elif attach == "404":
            try:
                randname = f"{randomchar(random.randrange(6, 12))}.pdf"
                pdf = PDF('P', 'mm', 'A5')
                pdf.set_title(corp)
                pdf.set_author(fullname)
                pdf.set_auto_page_break(auto=True, margin=15)
                pdf.print_chapter(link, fullname, position, corp, subordermsg, footer, location, cell, vcorp)
                pdf.output(f"{os.path.dirname(os.path.realpath(__file__))}/attached/{randname}")
            except Exception as ep:
                print(ep)
                pass
            else:
                attachment = open(str(f"{os.path.dirname(os.path.realpath(__file__))}/attached/{randname}"), 'rb')
                part3 = MIMEBase('application', 'octet-stream')
                part3.set_payload((attachment).read())
                encoders.encode_base64(part3)
                attachname = os.path.basename(str(randname))
                part3.add_header('Content-Disposition', 'attachment; filename="%s" ' % attachname)
                msg.attach(part3)

        if sendmode == 1:
            with smtplib.SMTP_SSL(smtp_server, port) as mailer:
                #mailer.starttls()
                mailer.login(smtpuser, smtp_pass)
                mailer.sendmail(me, email, msg.as_string())
                print(f'{me} sent email to {email} | sucessfully')
                mailer.quit()
        else:
            with smtplib.SMTP('localhost', 25) as mailer:
                mailer.sendmail(me, email, msg.as_string())
                print(f'{me} sent email to {email} | sucessfully')
                mailer.quit()
        xkey = f"keY-{getpass.getuser().capitalize()}TimePa$$"
        c300 = decrypt(xkey)
        c300 = c300.split(",")
        count = int(c300[0]) + 1
        limit = int(c300[1])
        now = c300[2]
        if count >= limit:
            now = datetime.today()
        updateLicence(count, limit, now)
    except KeyboardInterrupt:
        pauseClass()
        pass
    except Exception as ex:
        print(f"Something went wrong….\n {ex}\nskipping {email}\n")
        pass
    tsleep(1)
    successcount += 1


lead()
attach = str(input("Add attachment?\n1.Yes\n2.No\n::>"))
if attach == "1":
    xatt = input("1. Enter Path of Your Attachment\n2. Generate PDF Attachment\n::> ")
    if xatt == "1":
        filename = str(input(f"Enter Path/Name of your attachment::>{str(Path.home())}/"))
    elif xatt == "2":
        attach = "404"
    else:
        print("Invalid selection")
        sys.exit(3)

os.system('clear')
for lead in leads:
    mailer(lead['email'], lead['vname'], lead['vcorp'])


print("\nemails sent completely \n")
tsleep(15)
os.system('clear')

sys.exit()
