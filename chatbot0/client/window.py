import tkinter
import sys

sys.path.insert(1, 'connection/tcp')

from client import Client

class Window(Client):

    def __init__(self):

        self.root = tkinter.Tk()

        self.txt = tkinter.Text(self.root)
        self.txt.grid(column=0, row=0, columnspan=2)

        self.entry = tkinter.Entry(self.root, width=100)
        self.entry.grid(row=1, column=0)

        self.send_button = tkinter.Button(
            self.root, text="send", command=self.send)
        self.send_button.grid(row=1, column=1)

        Client.__init__(self)

    def send(self):

        #send message to the server
        answer = self.write(self.entry.get())

        send = "tu: "+ self.entry.get()
        res = "bot: "+ str(answer)
        self.txt.insert(tkinter.END, "\n"+send)
        self.txt.insert(tkinter.END, "\n"+res)
        self.entry.delete(0, tkinter.END)

    def show(self):
        self.root.title("chatbot")
        self.root.mainloop()