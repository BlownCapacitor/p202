import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected! Get ready!")
class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("QUIZ!")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=300, height=200, bg= "coral")

        self.pls = Label(self.login,
                         text="Login:",
                         justify=CENTER,
                         font="Helvetica 14 bold", bg = "cyan")
        self.pls.place(relheight=0.1,
                       relx=0.2,
                       rely=0.07)

        self.labelName = Label(self.login,
                               text="Name: ",
                               font="Helvetica 12" , bg = "cyan")
        self.labelName.place(relheight=0.2,
                             relx=0.1,
                             rely=0.2)

        self.entryName = Entry(self.login,
                               font="Helvetica 14")
        self.entryName.place(relwidth=0.4,
                             relheight=0.12,
                             relx=0.35,
                             rely=0.2)
        self.entryName.focus()

        self.inButton = Button(self.login, text="Start", font="Helvetica 14 bold",
                               command=lambda: self.goAhead(self.entryName.get()))
        self.inButton.place(relheight=0.12, relwidth=0.4, relx=0.35, rely=0.4)
        self.Window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.nickName = name
        receive_thread = Thread(target=self.receive)
        receive_thread.start()

    def receive(self):
      while True:
          try:
              message = client.recv(2048).decode('utf-8')
              if message == 'NICKNAME':
                  client.send(self.nickName.encode('utf-8'))
              else:
                  pass
          except:
              print("An error occured!")
              client.close()
              break


g = GUI()
