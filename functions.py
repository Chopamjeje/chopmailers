# !/usr/bin/python
# coding=utf-8

# imports
from bigVar import *
import random
import sys
import os
from pathlib import Path
import getpass
import base64
import time
from time import sleep as tsleep
from datetime import datetime, timedelta
import re
import hashlib

xlinks = []
bigflame = ""
defsub = ""
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
leads = []
htmlmsg = ""
attach = ""
filename = ""


def replace_placeholders(text):
    pattern = r'\{{[^}]*\}}'
    return re.sub(pattern, lambda match: str(eval(match.group(0)[2:-2])), text)


def randomchar(length):
    px = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
          "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    return ''.join(random.choices(px, k=length))


def randomString(length):
    px = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
          "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    return ''.join(random.choices(px, k=length))


def base64enc(word):
    return str(base64.b64encode(word.encode('ascii')).decode('ascii'))


def md5email(email):
    salt = "pX-Toolx"
    email = email.lower().strip()
    fin = f"{email}{salt}"
    return hashlib.md5(fin.encode('utf-8')).hexdigest()


def updateLicence(count, limit, now):
    xkey = f"keY-{getpass.getuser().capitalize()}TimePa$$"
    xall = f"{count},{limit},{now}"
    xsall = bytes(xall, 'utf-8')
    gxfile = f"{os.path.dirname(os.path.realpath(__file__))}/licences/{getpass.getuser()}.licence"
    xindex = 0
    xmax_index = len(xkey) - 1
    try:
        with open(gxfile, 'wb') as f:
            for xbyte in xsall:
                xxor_byte = xbyte ^ ord(xkey[xindex])
                f.write(xxor_byte.to_bytes(1, 'little'))
                if xindex >= xmax_index:
                    xindex = 0
                else:
                    xindex += 1
    except Exception as ex:
        print(ex)


def decrypt(key):
    cla = ""
    file = f"{os.path.dirname(os.path.realpath(__file__))}/licences/{getpass.getuser()}.licence"
    index = 0
    max_index = len(key) - 1

    try:
        with open(file, 'rb') as f:
            data = f.read()
            for byte in data:
                xor_byte = byte ^ ord(key[index])
                ml = xor_byte.to_bytes(1, 'little')
                cla = f"{cla}{ml.decode('utf-8')}"
                if index >= max_index:
                    index = 0
                else:
                    index += 1
    except Exception as ex:
        print(ex)
    return cla


def check():
    cla = decrypt(f"keY-{getpass.getuser().capitalize()}TimePa$$")
    gle = cla.split(",")
    if (datetime.strptime(gle[2], '%Y-%m-%d %H:%M:%S.%f') + timedelta(1) < datetime.today()):
        updateLicence(0, gle[1], datetime.today())
    else:
        if (int(gle[0]) >= int(gle[1])):
            os.system('clear')
            dateimp = \
                str((datetime.strptime(gle[2], '%Y-%m-%d %H:%M:%S.%f') + timedelta(1)) - datetime.today()).split(".")[0]
            remainz = dateimp.split(":")
            print(
                f"You have exceeded your daily limit of {int(gle[1])} mails. \nPlease wait till {str(datetime.strptime(gle[2], '%Y-%m-%d %H:%M:%S.%f') + timedelta(1)).split('.')[0]} to send more mails\n\nCurrent Time : {str(datetime.today()).split('.')[0]}")
            if (int(remainz[0]) <= 0):
                print(f"Time Remaining: {remainz[1]} minutes, {remainz[2]} seconds\n\n")
            elif (int(remainz[0]) <= 0 and int(remainz[1]) <= 0):
                print(f"Time Remaining: {remainz[2]} seconds\n\n")
            else:
                print(f"Time Remaining: {remainz[0]} hours, {remainz[1]} minutes, {remainz[2]} seconds\n\n")
            tsleep(5)
            sys.exit()


def pauseClass():
    input("Press the <ENTER> key to continue...")


def getlinks(email):
    link = ""
    codex = base64enc(email)
    replaceable = {
        '{email}': f'{email}',
        '{codex}': f'{codex}'
    }
    try:
        with open(f"{str(Path.home())}/links.txt", 'r', encoding='utf-8') as f:
            filelink = f.read()
            filelink = filelink.split(",")
            for x in filelink:
                xlinks.append(x)
        #link = f"http://{randomchar(random.randint(5,15))}.{linker}/?0=0&conf_id={base64enc(email)}"
        #link = f"http://{comrgen()}-{randomchar(random.randint(5,15))}.{linker}/?0=0&conf_id={base64enc(email)}"        
        #link = f"http://{comrgen()}-{randomchar(random.randint(5,15))}.{linker}/?x=y&codex={base64enc(email)}"                
        #link = f"https://{linker}/?0=0&conf_id={base64enc(email)}"                
        link = f"https://{random.choice(xlinks)}/?action={codex}"        
        #link = f"https://{random.choice(xlinks)}/#{codex}"        
        #link = f"http://{randomchar(random.randint(4, 16))}.{random.choice(xlinks)}/?0=0&conf_id={base64enc(email)}"
    except Exception as ex:
        print(ex)

    return link


def company():
    c2 = random.choice(c)
    return c2


def countrys():
    c2 = f"{random.choice(countries)}"
    return c2


def streets():
    c2 = f"{random.choice(address)}"
    return c2


def greetings():
    ln1 = ["good"]
    ln2 = ["day", "morning", "afternoon"]
    ln3 = ["I hope"]
    ln4 = ["you're", "you are", "you"]
    ln5 = ["enjoying your", "having a", "doing"]
    ln6 = ["well", "great", "wonderful"]
    ln7 = ["day", "week", "time"]
    greeting = random.choice(ln1) + " " + random.choice(ln2) + ", \n" + random.choice(ln3) + " " + random.choice(
        ln4) + " " + random.choice(ln5) + " " + random.choice(ln6) + " " + random.choice(ln7) + ". \n"
    return greeting


def footers():
    ln1 = ["I", "We"]
    ln2 = ["hope"]
    ln3 = ["we will", "we can", "we"]
    ln4 = ["have a", "have"]
    ln5 = ["good", "nice", "long"]
    ln6 = ["cooperation", "partnership", "collaboration"]
    ln7 = ["with you", "with your company"]
    footer = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(
        ln4) + " " + random.choice(ln5) + " " + random.choice(ln6) + " " + random.choice(ln7) + ".\n"
    return footer


def subordermsgs():
    ln1 = ["Please", "kindly", "help"]
    ln2 = ["view", "see", "review", "check"]
    ln3 = ["attach", "attached", "annex", "attachment"]
    ln4 = ["file", "document", "information", "specification"]
    ln5 = ["below", "under", "underneath", "beneath"]
    ln13 = ["stating our total quantity, Drawing and specification", "about our quantity and Drawing"]
    ln14 = ["also", "with"]
    ln15 = ["the price we"]
    ln16 = ["can", "have"]
    ln17 = ["offered", "offer"]
    ln18 = ["on the"]
    ln19 = ["PO", "order", "deal", "purchase"]
    ln20 = ["according to what our budget is.", "according to our budget."]
    ln6 = ["if", "whether", "to know if"]
    ln7 = ["you", "your company", "your organisation"]
    ln8 = ["can", "will be able to"]
    ln9 = ["meet", "reach"]
    ln10 = ["the"]
    ln11 = ["specific product", "product"]
    ln12 = ["and quantity", "quantity", "quality"]
    suborder = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(
        ln4) + " " + random.choice(ln5) + " " + random.choice(ln13) + " " + random.choice(ln14) + " " + random.choice(
        ln15) + " " + random.choice(ln16) + " " + random.choice(ln17) + " " + random.choice(ln18) + " " + random.choice(
        ln19) + " " + random.choice(ln20) + " " + random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(
        ln6) + " " + random.choice(ln7) + " " + random.choice(
        ln8) + " " + random.choice(ln9) + " " + random.choice(ln10) + " " + random.choice(ln11) + " " + random.choice(
        ln12) + ". \n"
    return suborder


def submsg():
    subm1 = ['would', 'will']
    subm2 = ['like', 'seek', 'love', 'want']
    subm3 = ['to']
    subm4 = ['have', 'conduct']
    subm5 = ['business', 'profession', 'trade', 'craft', 'trading', 'commerce', 'buying and selling', 'dealing',
             'marketing', 'merchandising', 'bargaining', 'transactions', 'negotiations', 'proceedings']
    subm6 = ['discussion', 'conversation', 'talk', 'dialogue', 'discourse', 'conference', 'deliberation',
             'consultation']
    subm7 = ['with you', 'about your company', 'about your products', 'about your business']
    subm = random.choice(subm1) + ' ' + random.choice(subm2) + ' ' + random.choice(subm3) + ' ' + random.choice(
        subm4) + ' ' + random.choice(subm5) + ' ' + random.choice(subm6) + ' ' + random.choice(subm7)
    return subm


def randint(lent):
    px = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    return ''.join(random.choices(px, k=lent))


def posgen():
    title = ['Manager', 'Director', 'CEO', 'Sales', 'Import Manager', 'Dealer', 'Supplier', 'Export Manager',
             'Chairman', 'Sales Rep', 'Purchase Rep', 'Chief', 'Co-Founder', 'Co-Founder', 'Purchase', 'President',
             'Marketing Director', 'Marketing Manager', 'Product manager', 'Sales Agent', 'Buyer', 'Purchase Manager',
             'Export Assistant', 'Regional Sales Manager', 'Store Manager', 'Senior Sales Manager', 'Senior Purchaser',
             'Project Manager', 'Purchaser']
    return random.choice(title)


def namegen():
    name = random.choice(s1) + ' ' + random.choice(s1)
    return name


def lead():
    fugazi = set()
    invalid = {"@snov.io", "getresponse", "unsubscribe", "bounce", "postmaster", "passport", "alibaba", "made-in-china", "tawk.", "@gmail.", "reply", "noreply", ".edu.", "@qq.com", "promotion", "aliexpress", "admin", "webmaster", "report", "abuse", "google", "@navercorp.com"}
    filename = f"{str(Path.home())}/leads.txt"
    try:
        with open(f'{filename}', 'r') as f:
            with open(f"{os.path.dirname(os.path.realpath(__file__))}/leads/{os.getlogin()}.txt", "a",
                      encoding="UTF-8") as gf:
                for items in f:
                    try:
                        items_list = items.split("|")
                        if len(items_list) == 1:
                            email = str(items_list)
                            vname = ""
                            vcorp = ""
                        elif len(items_list) == 2:
                            email, vname = items_list
                            vcorp = ""
                        elif len(items_list) == 3:
                            email, vname, vcorp = items_list
                        email = re.search(EMAIL_REGEX, str(email))
                        email = email.group(0)
                        email = email.lower()
                        if email not in fugazi and next((True for ban in invalid if ban in email), False) is False:
                            leadsinfo = {}
                            leadsinfo['email'] = email.strip()
                            leadsinfo['vname'] = vname.strip()
                            leadsinfo['vcorp'] = vcorp.strip()
                            leads.append(leadsinfo)
                            fugazi.add(email)
                            gf.write(f"{email}|{vname}|{vcorp}\n")
                    except Exception as e:
                        print(e)
                        pass
    except Exception as ex:
        print(f"error, ({filename}) is not correctly formated.\n")
        print(ex)
        sys.exit()


def generate_html_message(link):
    ln1 = ["Hello,", "Hi,", "Dear,", "Greetings,"]
    ln2 = ["we", "our team"]
    ln3 = ["would like to place", "are interested in placing"]
    ln4 = ["an order for", "a purchase order for"]
    ln5 = ["the following items:", "the items listed below:"]
    greeting = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(ln4) + " " + random.choice(ln5)

    ln1 = ["Please", "kindly"]
    ln2 = ["view", "see"]
    ln3 = ["the attached", "the enclosed"]
    ln4 = ["files", "documents"]
    ln5 = ["for more information.", "for further details."]
    suborder = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(ln4) + " " + random.choice(ln5)

    ln1 = ["We", "Our company"]
    ln2 = ["hope", "believe"]
    ln3 = ["this order will", "we can"]
    ln4 = ["be", "prove to be"]
    ln5 = ["beneficial", "profitable", "satisfactory"]
    ln6 = ["for both parties.", "for our business relationship."]
    footer = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(ln4) + " " + random.choice(ln5) + " " + random.choice(ln6)

    # Generating the message with styles
    message = f"""
        <div><!-- style="background-color: #f7f7f7; padding: 20px; font-family: Arial, sans-serif;">-->
            <p style="font-size: 16px; font-weight: bold; margin: 0;">{greeting}</p>
            <p style="font-size: 14px; margin-top: 10px;">{suborder}</p>
            <p style="font-size: 14px; margin-top: 10px;">{footer}</p>
            <p style="font-size: 14px; margin-top: 10px;">Please find the link to the order files:>> <a href='{link}' style="color: #008cba;">{link}</a></p>
            <br>
        </div>
    """

    return message

def generate_table_message():
    ln1 = ["Hello", "Hi", "Greetings"]
    ln2 = ["Friend", "Dear"]
    person = random.choice(ln1) + " " + random.choice(ln2)

    ln1 = ["good"]
    ln2 = ["day", "morning", "afternoon"]
    ln3 = ["I hope"]
    ln4 = ["you're", "you are", "you"]
    ln5 = ["enjoying your", "having a", "doing"]
    ln6 = ["well", "great", "wonderful"]
    ln7 = ["day", "week", "time"]
    greeting = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(ln4) + " " + random.choice(ln5) + " " + random.choice(ln6)+ " " + random.choice(ln7)

    ln1 = ["I", "we", "our team", "my company", "our client", "my costumers", "my client", "our costumers",]
    ln2 = ["would like to place", "are interested in placing", "want to place"]
    ln3 = ["an order", "a purchase order", "urgent order"]
    ln4 = ["can you", "please", "Could you"]
    ln5 = ["comfirm", "provide", "authenticate", "substantiate"]
    ln6 = ["updated", "your",  "validate", "verified"]
    ln7 = ["price list", "payment method", "lastest pettern", "sutaible price list for resellers"]
    messages = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(ln4) + " " + random.choice(ln5) + " " + random.choice(ln6) + " " + random.choice(ln7)

    ln1 = ["Please", "kindly", "help"]
    ln2 = ["view", "see", "review", "check"]
    ln3 = ["attach", "attached", "annex", "attachment"]
    ln4 = ["file", "document", "information", "specification"]
    ln5 = ["below", "under", "underneath", "beneath"]
    ln6 = ["spec", "sample", "specfication"]
    ln7 = ["according to what our budget is.", "according to our budget."]
    ln8 = ["if", "whether", "to know if"]
    ln9 = ["you", "your company", "your organisation"]
    ln10 = ["can", "will be able to"]
    ln11 = ["meet", "reach"]
    ln12 = ["the"]
    ln13 = ["clients", "costumer", "buyer"]
    ln14 = ["specific product", "product"]
    attach = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(ln4) + " " + random.choice(ln5) + " " + random.choice(ln6) + " " + random.choice(ln7) + " " + random.choice(ln8) + " " + random.choice(ln9) + " " + random.choice(ln10) + " " + random.choice(ln11) + " " + random.choice(ln12) + " " + random.choice(ln13) + " " + random.choice(ln14)

    ln1 = ["also", "but before then", "can you"]
    ln2 = ["Please", "kindly"]
    ln3 = ["comfirm", "verify"]
    ln4 = ["availability and ETD", "if this is the right email to contact", "payment method", "your company legally registered"]
    suborder = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(ln4)

    ln1 = ["We", "Our company"]
    ln2 = ["hope", "believe"]
    ln3 = ["this order will", "we can"]
    ln4 = ["be", "prove to be"]
    ln5 = ["beneficial", "profitable", "satisfactory"]
    ln6 = ["for both parties.", "for our business relationship."]
    footer = random.choice(ln1) + " " + random.choice(ln2) + " " + random.choice(ln3) + " " + random.choice(ln4) + " " + random.choice(ln5) + " " + random.choice(ln6)

    # Generating the message with styles
    message = f"""
        <div><!-- style="background-color: #f7f7f7; padding: 20px; font-family: Arial, sans-serif;">-->
        <P>{person}<BR>{greeting}<BR>am soucring agent for all this companies in the attachment<BR>{attach}<BR>{footer}</P></BODY></HTML>
            <br>
        </div>
    """

    return message

def read_smtp_file():
    file_path = f"{str(Path.home())}/smtp.txt"
    smtp_list = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                count_pipe = line.count("|")
                if count_pipe == 3:
                    smtp_data = line.split('|')
                    smtp_dict = {
                        'smtpserver': smtp_data[0],
                        'smtpuser': smtp_data[1],
                        'smtppass': smtp_data[2],
                        'smtpport': smtp_data[3]
                    }
                    smtp_list.append(smtp_dict)
                else:
                    print(f"Warning: Invalid line with {count_pipe} values: {line}")
    return smtp_list

def get_domain():
    file_path = f"{str(Path.home())}/domains.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            domainlist.append(line.strip())
            

def get_image():
    file_path = f"{str(Path.home())}/image.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            imagelist.append(line.strip())
