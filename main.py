from utils import Email
from colorama import Fore
from time import sleep
import requests


email = Email(proxy=False)
print("Check proxy...    ", end = "")
if email.check_proxy() == False:
    print(Fore.RED+f"        [ERROR]{Fore.WHITE}")
    exit("Please enter valid proxy!")
else:
    print(Fore.GREEN + f"        [OK]{Fore.WHITE}")
stat = email.generate_email()
if stat[0] == "error":
    exit("Error!        [GENERATE EMAIL]")
mail, login, domain = stat
print(f"Email: {mail}")
mess = []
while True:
    data = email.get_inbox(login, domain)
    if len(data) != 0 and data not in mess:
        mess.append(data)
        print("New message!")
        mess_id = data[0]['id']
        who = data[0]['from']
        stat = email.get_message(mail, mess_id)
        if stat[0] == False:
            print("Error!        [PARSE MESSAGE]")
        else:
            s,who,text,subject,date = stat
            print(f"Date: {date}\nFrom: {who}\nText: {text}\nSubject: {subject}\n--------------")
            try:
                if "http" in text.lower():
                    f = text.split("http")[1].split("<")[0].split()[0].split(",")[0]
                    url = f"http{f}"
                    b  =requests.get(url)
                    print(f"Find url: {url}")
            except:
                pass

    sleep(8)


