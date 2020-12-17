import tkinter
from tkinter import messagebox
from threading import Thread
from tkinter import *
from time import sleep
import PIL.Image
import PIL.ImageTk
from utils import Email
image_name = "image.png"
root = Tk()
root.title("Faker Email Assistant  [V 1.0]")
root.resizable(False, False)
root.geometry("800x500")
#########################################################
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = image_name)
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#########################################################
def doch():
    top = Toplevel()
    top.title("Create email")
    top.geometry("250x70")
    l = Label(top,text = "Please wait...", font = "Consolaas 20")
    l.pack()
    
    def Main():
        #root.after(200, Main)
        email = Email()
        stat=email.generate_email()
        while stat[0] == "error":
            messagebox.showerror("Error", "An error occured while generating mail")
            stat = email.generate_email()
            sleep(5)
        #else:
        def copy():
            top.clipboard_clear()
            top.clipboard_append(mail)
        mail, login, domain = stat
        top.title(mail)
        l.destroy()
        t = Text(top,height=1, borderwidth=0)
        t.insert(1.0, f"Your mail addres: ")
        t.place(x = 5, y = 5)
        t.configure(state="disabled")
        t.configure(inactiveselectbackground=t.cget("selectbackground"), relief = "flat")
        t.configure(width=35)
        top.geometry("550x350")
        b = Button(top, text = mail, command = copy)
        b.place(x = 150, y = 5)
        lab = Label(top, text = "No letters yet", font = "Consolaas 20")
        lab.place(x = 8, y = 50)
        def pp():
            x = 8
            y = 50
            lit = []
            def get_mess(text):
                id = int(text.split("(")[1].split(")")[0])
                text = email.get_message(mail, id)
                pop = Toplevel()
                pop.geometry("400x300")
                pop.title("New message")
                popo = Text(pop)
                popo.pack()
                popo.insert(1.0, f"Date: {text[4]}\nFrom: {text[1]}\nSubject: {text[3]}\nText: {text[2]}\n")
                pop.mainloop()
            while True:
                lp = email.get_inbox(login, domain)
                if len(lp) != 0:
                    lab.destroy()
                    for p in lp:
                        if p not in lit:
                            lit.append(p)
                            b = Button(top, text = f"{lp[0]['from']}  ({lp[0]['id']})", command = get_mess(f"{lp[0]['from']}  ({lp[0]['id']})"))
                            b.place(x = x, y = y )
                            y += 30
                sleep(2)
        Thread(target=pp).start()

        
    top.after(100, Main)
    top.mainloop()
Button(text = "Create new email", font = "Consolaas 20", bg = "#006098", fg = "white", command = doch).place(x = 285, y = 50)
root.mainloop()



