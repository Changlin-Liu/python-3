#! /usr/bin/env python
#! -*- coding:utf-8 -*-
from tkinter import *
root = Tk()
root.title('Lable test')
# 默认情况下文本居中显示，通过justify设置文字左对齐
# bg北京色，fg前景色，width、height背景宽高
Label(root, text='www.admin.com',
    bg='yellow', width=30, height=4,
    wraplength=100, justify="left").pack()
# anchor设置文本左边显示，通过justify设置文字右对齐
Label(root, text='m.admin.com',
    bg='red', width=35, height=4,
    wraplength=100, anchor='w', justify='right').pack()
# relief设置label外观，wraplength设置一行显示的字符数
Label(root, text='mapp.admin.com',
    bg='blue', width=40, height=4,
    wraplength=100, anchor='e', relief='ridge').pack()
root.mainloop()