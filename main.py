#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Time    : 2023/4/8 11:44 AM
    @Author  : majiayang
    @File    : main.py
    @Software: PyCharm Community Edition

"""
from tkinter import *
from datetime import datetime

root = Tk()

w = Label(root,text="",font=('微软雅黑',100,"bold"),anchor=CENTER,background="#008CBA",foreground="white")
w.pack(fill=BOTH,expand=True)

# root.geometry("1920x1080+0+0")
root.attributes("-fullscreen", True)
# root.config(cursor="none")


def get_time():
    t =  str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    w.config(text = t)
    w.after(1000,get_time)

get_time()

root.mainloop()

