from tkinter import *
import tkinter.messagebox as messagebox

class Appliaction(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        # 以类方法的形式，将子widget[application]加入到父容器Frame并显示
        self.pack()
        # 以类方法的形式，将子widget[label/button]加入父容器并显示
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        # pack方法吧widget加入到父容器
        self.nameInput.pack()
        self.altertButton = Button(self, text='Hello', command=self.hello)
        self.altertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)
# 实例化application
app = Appliaction()
# 设置窗口名称
app.master.title('Hello World')
# 设置消息主循环
app.mainloop()
