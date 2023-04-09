#Integreate A,B,C game into one as a console
import sys
import os
import tkinter as tk
from tkinter import ttk
import A_tictactoe as A
import B_hangmantile as B
import C_pianotiles as C

#setting up the frame for dashboard
root=tk.Tk()
root.title("Arcade Game Console")
root.geometry('500x500')
frm=ttk.Frame(root,padding=20)
frm.grid()
#ttk.Label(frm, text="Hello World!").grid(column=0,row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
def open_A():
    os.system('A_tictactoe.py')
def open_B():
    os.system('B_hangmantile.py')
def open_C():
    os.system('C_pianotiles.py')
A_but=ttk.Button(frm, text="TIC TAC TOE", command=open_A)
B_but=ttk.Button(frm, text="HANGMAN TILES", command=open_B)
C_but=ttk.Button(frm, text="PIANO TILES", command=open_C)
quit=ttk.Button(frm, text="QUIT", command=root.destroy)
A_but.grid(column=1,row=0)
B_but.grid(column=4,row=0)
C_but.grid(column=7,row=0)
quit.grid(column=9,row=4)
root.mainloop()
