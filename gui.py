# -*- coding: utf-8 -*-
from input import input2
from app import name
from crftest import CRFTEST1
from output import output1
import tkinter as tk
import os
top=tk.Tk()
top.title('中文电子病历实体识别')
top.resizable(0, 0)
top.geometry('1550x350')
top.geometry('+150+250')
e=tk.Entry(top,font = ('Times', '30', 'bold'),width = 300)
e.pack()
def insert_point():
    var=e.get()
    input2(var)
    CRFTEST1()
    name()
    output1()
    datafile=os.getcwd()+"/最后文本2.txt"
    data=open(datafile,"r")
    data1=data.read()
    t.insert('end',data1)
b1=tk.Button(top,text='实体提取',width=15,height=2,command=insert_point)
b1.pack()
t=tk.Text(top,font = ('Times', '30', 'bold'),height=6,width=10000)
t.pack()

top.mainloop()













