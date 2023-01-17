

"""

   ____             __                  ____  _     _     _                      

  / ___|___  _ __  / _|_   _ ___  ___  |  _ \| |__ (_)___| |__   ___ _ __ ___    

 | |   / _ \| '_ \| |_| | | / __|/ _ \ | |_) | '_ \| / __| '_ \ / _ | '__/ __|   

 | |__| (_) | | | |  _| |_| \__ |  __/ |  __/| | | | \__ | | | |  __| |  \__ \   

  \____\___/|_| |_|_|  \__,_|___/\___| |_|   |_| |_|_|___|_| |_|\___|_|  |___/   

  _             ____           _     _            __  __      _     _            

 | |__  _   _  |  _ \ _ __ ___(_)___| |_ ___ _ __|  \/  | ___(_)___| |_ ___ _ __ 

 | '_ \| | | | | | | | '__/ _ | / __| __/ _ | '__| |\/| |/ _ | / __| __/ _ | '__|

 | |_) | |_| | | |_| | | |  __| \__ | ||  __| |  | |  | |  __| \__ | ||  __| |   

 |_.__/ \__, | |____/|_|  \___|_|___/\__\___|_|  |_|  |_|\___|_|___/\__\___|_|   

        |___/                                                                   

"""



import names

import requests

import random

import time



# URL die versucht Daten zu stehlen

target_url = input("Phishing URL: ")

# verschiedene Email-Hosts um Phisher zu verwirren

emails = ["outlook.de", "outlook.com", "outlook.ch", "googlemail.com", "mail.co.uk", "orange.fr", "gmail.fr", "gmail.com","gmx.ch", "gmx.net", "web.de", "yahoo.com", "hotmail.com", "aol.com", "hotmail.co.uk", "hotmail.fr", "msn.com", "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", "yahoo.co.uk", "yahoo.com.br", "yahoo.co.in", "live.com", "rediffmail.com", "free.fr"]

# Wordlist muss im selben Pfad wie das Script abgespeichert sein und darf nur im UTF-8 Format sein!

fileinput = input("Type wordlist name: ")

with open(fileinput, 'r') as liste:

	wlist = liste.readlines()

counter = 0



def send_random_request():

    global counter

# generiert Random Namen und hängt eine zufällige Mailendung an

    email = names.get_full_name().replace(" ", ".") + "@" + random.choice(emails)

    password = ''.join(random.choice(wlist))

    payload = {"email":email,"password":password}

    result = requests.post(target_url, allow_redirects=False, data=payload)

    counter += 1

    print(f"Sending No.{counter}: {email} and {password}")

    print(result)



if __name__ == "__main__":

    while True:

        send_random_request()

        time.sleep(random.randint(1,500)/10)

       



