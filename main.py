# Integreate A,B,C game into one as a console
import subprocess
from tkinter import *

# setting up the frame for dashboard
root = Tk()
root.title("Arcade Game Console")
#bg = PhotoImage(file = "download.jpg")
root.geometry('500x500')
#frame1 = Frame(root, padding=20)
#frame1.grid()
#root.iconphoto(False, PhotoImage(file="E:\Studies\UOP\E20\Semester 2\GP 106 Computing\Project\Arcade-Game-Console\a.png"))
# ttk.Label(root, text="Hello World!").grid(column=0,row=0)
# ttk.Button(root, text="Quit", command=root.destroy).grid(column=1, row=0)

def run_A():
    subprocess.run(["python", "A_tictactoe.py"])
def run_B():
    subprocess.run(["python", "B_hangmantile.py"])
def run_C():
    subprocess.run(["python", "C_pianotiles.py"])

#butttons for run the game
bt1 = Button(
    root,
    text="TIC TAC TOE",
    command=run_A
)
bt2 = Button(
    root,
    text="HANGMAN TILES",
    command=run_B
)
bt3 = Button(
    root,
    text="PIANO TILES",
    command=run_C
)
quit = Button(
    root,
    text="QUIT",
    command=root.destroy
)
bt1.grid(column=1, row=0)
bt2.grid(column=4, row=0)
bt3.grid(column=7, row=0)
quit.grid(column=9, row=4)

root.mainloop()
