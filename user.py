# CREATED BY WILSON JUNIOR
# IBIAPINA-CEARA, 15/07/2017

from Tkinter import *
import ttk
import tkMessageBox
import imaplib
import email.header
import email
from unicodedata import normalize
from email.header import decode_header


class user:
    app=""
    usuario=""
    senha=""
    server="outlook.office365.com"
    mail=""
    tofrom=[]
    subjects=[]
    titulos=""
    input=""
    corpo_emails=[]
    email=""
    label_from=""


    def __init__(self,usuario,senha,server,port):
        self.app = Tk(className='Pagina Inicial do Usuario')
        self.app.resizable(width=False,height=False)


        self.usuario = usuario
        self.senha = senha


        self.header(self.app)
        self.body(self.app)

        self.app.mainloop()

    def header(self,master):
        painel_header = Frame(master)
        painel_header.pack(side=TOP)
        titulo = Label(painel_header,text='Pagina do Usuario',font='Serif 12 bold')
        titulo.pack(side=TOP)

        usuario = Label(painel_header, text="Ola! Seja bem vindo " + str(self.usuario), font='Comic 10 italic')
        usuario.pack()

    def body(self,master):
        painel_emails = Frame(master)
        painel_emails.pack(fill='x')

        subjects = []
        try:

            self.mail = imaplib.IMAP4_SSL(self.server)
            self.mail.login(self.usuario,self.senha)

            self.mail.select("inbox")
            result,data = self.mail.search(None,"ALL")
            ids = data[0].split()

            for id in ids:
                result,data = self.mail.fetch(id,"RFC822")
                string = data[0][1]
                string = email.message_from_string(string)
                self.subjects.append(decode_header(string['Subject'])[0][0].decode("utf-8"))
                self.tofrom.append(decode_header(string['From'])[0][0].decode("utf-8"))
                body = ""
                for msg in string.walk():
                    if(msg.get_content_maintype()=="text"):
                        # msg.get_payload(None,True)
                        new_body = msg.get_payload(None,True)
                        body = ""+str(body)+""+str(new_body)+""
                self.corpo_emails.append(body)

            print len(self.corpo_emails)
            print len(self.tofrom)
        except:
            print "error"


        label_email = Label(painel_emails,text='Emails :')
        label_email.pack(side=LEFT)

        self.titulos = ttk.Combobox(painel_emails,values=self.subjects)
        self.titulos.current(0)
        self.titulos.pack(fill='x')

        painel_emails_option = Frame(master)
        painel_emails_option.pack(fill='x')
        label_busca = Label(painel_emails_option,text='Palavras-Chave para Busca :')
        label_busca.pack(side=LEFT)
        self.input = Entry(painel_emails_option)
        self.input.pack(fill='x')

        verificar_todos = Checkbutton(master,text='Verificar em todos os emails')
        verificar_todos.pack()

        palavras_separadas = Checkbutton(master,text='Verificar por palavra')
        palavras_separadas.pack()

        submit = Button(master,text='Buscar',width=30)
        submit.pack()
        submit.bind("<Button-1>",self.action_submit)

        self.label_from = Label(master,text=""+str(self.tofrom[0]).lower()+"",font='Comic 8 bold',padx=10,pady=10)
        self.label_from.pack(fill='x')

        self.email = Text(master,width=50,height=15,padx=10,pady=10)
        self.email.pack()
        self.email.insert(END,self.corpo_emails[0])

    def action_submit(self,event):
        for i in range(0,len(self.corpo_emails)):
            if(self.titulos.get() == self.subjects[i]):
                self.email.delete(1.0,END)
                self.email.insert(END,self.corpo_emails[i])
                name = normalize("NFKD",self.tofrom[i]).encode('ASCII','ignore').decode('ASCII')
                self.label_from.config(text=""+name+"")


        busca = str(self.input.get()).lower()
        busca = busca.split()
        for palavra in busca:
            for id in range(0,len(self.corpo_emails)):
                body = self.corpo_emails[id]
                body = str(body).lower()
                if(body.count(palavra)>0):
                    subject = normalize("NFKD",self.subjects[id]).encode('ASCII','ignore').decode('ASCII')
                    tkMessageBox.showinfo("PALAVRA ENCONTRADA","email "+str(subject)+"\n ""palavra :"+str(palavra)+"\n""ocorrencias :"+str(body.count(palavra))+" ")
