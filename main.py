# CREATED BY WILSON JUNIOR
# IBIAPINA-CEARA, 15/07/2017

from Tkinter import *
import poplib
import ttk
import tkMessageBox
import user

class main:
    email=""
    senha=""
    box=""
    port="995"
    app=""

    # OUTLOOK
    server="pop3.live.com"

    def __init__(self):
        self.app = Tk(className='AppReadMailer')
        self.app.resizable(width=False,height=False)

        frame_main = Frame(self.app,width=400,height=400,background='lightblue',padx=20,pady=20)
        frame_main.pack(side=TOP)

        self.header(frame_main)
        self.body(frame_main)
        self.app.mainloop()

    def header(self,master):
        title = Label(master,text='Aplicativo para Busca Automatica em Emails',bg='lightblue',fg='black',font='Monospace 15 bold')
        title.pack(side=TOP)

    def body(self,master):

        login = Frame(master,height=30,width=30,padx=10,pady=5,bg='lightblue',bd=10)
        login.pack(side=TOP)

        label_login = Label(login,bg='lightblue',padx=3,pady=3,text='Login de Acesso')
        label_login.pack(side=TOP)

        login_top = Frame(login,padx=10,pady=5,bg='lightblue')
        login_top.pack(side=TOP)
        label_email = Label(login_top,text='Email: ',bg='lightblue',font='Monospace 10 bold')
        label_email.pack(side=LEFT)
        self.email = Entry(login_top,width=40)
        self.email.pack(side=RIGHT)

        login_bottom = Frame(login,padx=10,pady=5,bg='lightblue')
        login_bottom.pack()
        label_senha = Label(login_bottom, text='Senha: ', bg='lightblue',font='Monospace 10 bold')
        label_senha.pack(side=LEFT)
        self.senha = Entry(login_bottom, width=40,show="*")
        self.senha.pack(side=RIGHT)

        login_server = Frame(login,padx=10,pady=10,bg='lightblue')
        login_server.pack()
        label_senha = Label(login_server, text='Servidor de Email: ', bg='lightblue', font='Monospace 10 bold')
        label_senha.pack(side=LEFT)
        self.box = ttk.Combobox(login_server,width=10)
        self.box['values'] = (['Outlook', 'Gmail'])
        self.box.current(0)
        self.box.pack(side=RIGHT)


        button = Button(master,text='Login',bg='green',fg='black',width=10,font='Monospace 10 bold')
        button.pack(side=BOTTOM)
        button.bind('<Button-1>',self.login)



    def login(self,event):
        usuario = self.email.get()
        senha = self.senha.get()
        if(usuario=='' or senha==''):
            tkMessageBox.showwarning('Campos Vazios','erro de leitura dos campos')
            self.email['bg'] = 'red'
            self.senha['bg'] = 'red'
        else:
            try:
                user.user(usuario,senha,'','')
            except:
                tkMessageBox.showerror('ERRO!','NAO ESTA AVANCANDO A JANELA DO USUARIO')




objeto = main()
