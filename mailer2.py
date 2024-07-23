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
    "What type of message do you want to send\n1. linkedin \n2. purcahse order \n3. payment \n4. quota \n5. big file. \n6. Alibaba. \n7. enter your subject. \n ::> "))

if sub == 7:
    defsub = str(input("Enter Your Subject \n ::> "))


get_domain()
get_image()

def subjectgen(type):
    subject = ""
    linkedin1 = ['Check', 'View', 'See']
    linkedin2 = ['business', 'urgent', 'invitation', 'request']
    linkedin3 = ['message', 'notice', 'mail', 'alert']
    linkedin4 = ['new', 'fresh']
    linkedin5 = ['immediately!', 'now!', 'quickly!']
    px1 = ['need', 'request', 'about', 'demand', 'regarding', 'send', 'attached']
    px2 = ['products', 'company', 'factory', 'supplier', 'organization', 'corp', 'manufacturer', 'industrial', 'firm']
    px3 = ['qoute', 'catalog', 'sample', 'pricelist', 'quotation', 'citation', 'production', 'sample', 'product', 'qoute', 'specifications', 'specimen', 'model', 'instance', 'prototype']
    quota1 = ['Mailbox', 'Mail', 'Account']
    quota2 = ['quota', 'storage', 'system space', 'available space']
    quota3 = ['low', 'very low', 'exhausted', 'below average']
    quota4 = ['Upgrade', 'Increase']
    quota5 = ['immediately!', 'now!', 'quickly!']
    payment0 = ['Fw:', 'Re:']
    payment1 = ['Kindly', 'please', 'hello,', 'greetings,']
    payment2 = ['Check', 'view']
    payment3 = ['bank']
    payment4 = ['reciept', 'slip']
    payment5 = ['for', 'about!', 'info,']
    payment6 = ['completed', 'advance', 'balance', 'partial']
    payment7 = ['payment']
    bigfile1 = ['Oversized', 'Big']
    bigfile2 = ['attachment', 'annex', 'file']
    bigfile3 = ['expiration', 'release', 'expire', 'expiring']
    bigfile4 = ['reminder', 'notice', 'alert']
    ali1  = ['see', 'review', 'kindly see']
    ali2 = ['buyers', 'client', 'companies']
    ali3 = ['contact', 'attachment', 'specfication', 'Order', 'information']
    # bigfile5 = ['immediately!', 'now!', 'quickly!']
    if type == 1:
        subject = random.choice(linkedin1) + ' ' + random.choice(linkedin4) + ' ' + random.choice(
            linkedin2) + ' ' + random.choice(linkedin3)
    elif type == 2:
        subject = random.choice(px1) + ' ' + random.choice(px2) + ' ' + random.choice(
            px3)  # "request for quotation" #random.choice(po2) + ' ' + random.choice(po1) + ' ' + random.choice(po3) + ' ' + random.choice(po4)
    elif type == 4:
        subject = random.choice(quota1) + ' ' + random.choice(quota2) + ' ' + random.choice(
            quota3) + ' ' + random.choice(quota4) + ' ' + random.choice(quota5)
    elif type == 3:
        subject = random.choice(payment0) + ' ' + random.choice(payment1) + ' ' + random.choice(
            payment2) + ' ' + random.choice(payment3) + ' ' + random.choice(payment4) + ' ' + random.choice(
            payment5) + ' ' + random.choice(payment6) + ' ' + random.choice(payment7)
    elif type == 5:
        subject = random.choice(bigfile1) + ' ' + random.choice(bigfile4) + ' ' + random.choice(
            bigfile2) + ' ' + random.choice(bigfile3)
    elif type == 6:
        subject = random.choice(ali1) + ' ' + random.choice(ali2) + ' ' + random.choice(
            ali3)
    elif type == 7:
        subject = defsub
    else:
        sys.exit()
    # print(subject)

    return subject


def mailer(x, y, z):
    successcount = 0
    check()
    email, vname, vcorp = x, y, z
    # amount = f"{phone(2)},{phone(3)}.{phone(2)}"
    pdate = str(datetime.today()).split(" ")[0]
    vdate = str(datetime.today() - timedelta(2)).split(" ")[0]
    adate = str(datetime.today() + timedelta(3)).split(" ")[0]
    #adate = str(datetime.today() + timedelta(3)).split(".")[0]
    name = namegen()
    subj = subjectgen(sub)
    corp = company()
    submessage = submsg()
    footer = footers()
    subordermsg = subordermsgs()
    greeting = greetings()
    country = countrys()
    street = streets()
    codex = base64enc(email)
    link = str(getlinks(email))

    pirand = str(randomString(random.randrange(2, 13)))

    domain = random.choice(domainlist)
    image = random.choice(imagelist)
    firstname = f"{name.split(' ')[0]}"
    lastname = f"{name.split(' ')[1]}"
    fullname = f"{firstname} {lastname}"
    cell = f"+{randint(random.randrange(2, 3))} ({randint(3)}) - {randint(7)}"
    fullemail = f"{lastname}{firstname}{randomchar(random.randrange(2, 8))}@{domain}"
    #fullemail = f"{lastname}_{firstname}.{randomchar(random.randrange(2, 8))}@{domain}"
    ccname = str(namegen())
    ccemail = f'{ccname.split(" ")[1]}.{ccname.split(" ")[0]}{domain}'
    cc = f'"{ccname}"({ccemail})'
    position = str(posgen())
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

    msg = MIMEMultipart('alternative')
    #msg['Subject'] = f"{userdomainfront.upper()} catalog and price list"
    #msg['Subject'] = f"{corp} enquiry for {userdomainfront.upper()} company"
    #msg['Subject'] = f"{userdomainfront.upper()} export"
    #msg['Subject'] = f"enquiry for {userdomainfront.upper()}"
    msg['Subject'] = f"{subj}"
    msg['From'] = me
    msg['To'] = email
    msg.add_header('reply-to', mex)

    text = f"see below information \n\n{link}\n\nThanks awaitng your quick action"  # text
    replaceable = {
        '{email}': f'{email}',
        '{domain}': f'{domain}',
        '{image}': f'{image}',
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
        '{submessage}': f'{submessage}',
        '{firstname}': f'{firstname}',
        '{lastname}': f'{lastname}',
        '{fullname}': f'{fullname}',
        '{greeting}': f'{greeting}',
        '{subordermsg}': f'{subordermsg}',
        '{footer}': f'{footer}',
        '{country}': f'{country}',
        '{street}': f'{street}',
        '{cell}': f'{cell}',
        '{codex}': f'{codex}',
        '{vname}': f'{vname}',
        '{vcorp}': f'{vcorp}',
        '{vdate}': f'{vdate}',
        '{pdate}': f'{pdate}',
        '{adate}': f'{adate}',
        '{pxrand}': f'<font id="{pirand}">{randomchar(random.randrange(2, 13))}&shy;{datetime.today()}</font>',
        '{pirand}': f'{pirand}',
        '{mex}': f'{mex}'
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
                   '.htm',
                   '.zip',
                   '.pdf',
                   '.xlsx',
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
                pdf.print_chapter(link, fullname, position, corp, subordermsg, footer, country, cell, vcorp)
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
            with smtplib.SMTP(smtp_server, port) as mailer:
                mailer.starttls()
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
