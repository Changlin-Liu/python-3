from tkinter import *
import tkinter.messagebox as messagebox


class Appliaction(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
    # def createWidgets(self):
        # self.nameInput = Entry(self)
        # self.nameInput.pack()
        # self.altertButton = Button(self, text='Hello', command=self.hello)
        # self.altertButton.pack()

    # def hello(self):
        # name = self.nameInput.get() or 'world'
        # messagebox.showinfo('Message', 'Hello, %s' % name)

app = Appliaction()
app.master.title('Hello World')
app.mainloop()
