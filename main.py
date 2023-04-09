#Integreate A,B,C game into one as a console
import tkinter as tk
from tkinter import ttk
import A_tictactoe as A
import B_hangmantile as B
import C_pianotiles as C

root=tk.Tk()
frm=ttk.Frame(root,padding=20)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0,row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
