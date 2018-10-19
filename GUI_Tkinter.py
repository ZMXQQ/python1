#!/user/bin/env python3
# coding:utf-8

'a GUI program by Tkinter'
__author__ = 'zmxqq'

from tkinter import *
import tkinter.messagebox as messagetbox
class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameIput = Entry(self)
        self.nameIput.pack()

        self.helloButton = Button(self, text='Hello,world!', command=self.hello)
        self.helloButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameIput.get() or 'world'
        messagetbox.showinfo('Message', 'hello, %s' % name)

app = Application()
app.master.title("Hello,world!")
app.mainloop()