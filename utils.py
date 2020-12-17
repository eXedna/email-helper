try:
    import requests
    import json
except Exception as e:
    print(f"CRITICAL ERROR [import error]: {e}")
    exit()

class Email:
    def __init__(self, proxy = None):
        self.url_generate = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
        self.url_messages = "https://www.1secmail.com/api/v1/?action=getMessages&login=LOGIN&domain=DOMAIN"
        self.url_message_data = "https://www.1secmail.com/api/v1/?action=readMessage&login=LOGIN&domain=DOMAIN&id=ID"
        self.tor_proxy= {"http" : "socks5://127.0.0.1:9050", "https" : "socks5://127.0.0.1:9050"}
        self.mail_list = []
        self.url_ipconfig = "https://ipconfig.me/ip"
        self.ses = requests.Session()
        if proxy:
            if str(proxy) != "False":
                if "http" in proxy or "socks" in proxy:
                    self.proxy = {"http" : proxy, "https" : "proxy"}
                else:
                    self.proxy = self.tor_proxy
            else:
                self.proxy = ""
        else:
            self.proxy = ""
    def check_proxy(self):
        if self.proxy != "":
            try:
                my_ip = requests.get(self.url_ipconfig, timeout = 7).text
                proxy_ip = requests.get(self.url_ipconfig, proxies = self.proxy, timeout = 7).text
                if my_ip == proxy_ip:
                    return False
                else:
                    return True
            except:
                return False

    def generate_email(self):
        try:
            r = self.ses.get(self.url_generate)
            mail = json.loads(r.content)[0]
            self.mail_list.append(mail)
            self.login = str(mail).split("@")[0]
            self.domain = str(mail).split("@")[1]
            return [mail, self.login, self.domain]
        except Exception as e:
            return ["error", e]
    def get_inbox(self, login, domain):
        url = self.url_messages.replace("LOGIN", login).replace("DOMAIN", domain)
        try:
            r = json.loads(self.ses.get(url).content)
            return r
        except:
            return "error"
    def get_message(self, mail, id):
        try:
            login, domain = map(str, mail.split('@'))
            mess_data =  json.loads(self.ses.get('https://www.1secmail.com/api/v1/?action=readMessage&login=%s&domain=%s&id=%i' % (login, domain, id)).content)
            who = mess_data['from']
            text = mess_data['body']
            subject = mess_data['subject']
            date = mess_data['date']
            return [True, who, text, subject, date]
        except Exception as e:
            return [False, e]
        
    


