# Integreate A,B,C game into one as a console
import subprocess
from tkinter import *

# setting up the frame for dashboard
root = Tk()
root.title("Arcade Game Console")
# bg = PhotoImage(file = "download.jpg")
root.geometry('500x500')
# frame1 = Frame(root, padding=20)
# frame1.place()
# root.iconphoto(False, PhotoImage(file="E:\Studies\UOP\E20\Semester 2\GP 106 Computing\Project\Arcade-Game-Console\a.png"))
# ttk.Label(root, text="Hello World!").place(x=0,y=0)
# ttk.Button(root, text="Quit", command=root.destroy).place(x=1, y=0)

# command function to run the game


def run_A():
    subprocess.run(["python", "A_tictactoe.py"])


def run_B():
    subprocess.run(["python", "B_hangmantile.py"])


def run_C():
    subprocess.run(["python", "C_pianotiles.py"])


# butttons for run the game
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
bt4 = Button(
    root,
    text="QUIT",
    command=root.destroy
)

# placing the buttons in the frame
bt1.place(x = 1, y = 0)
bt2.place(x = 4, y = 0)
bt3.place(x = 7, y = 0)
bt4.place(x = 9, y = 4)

root.mainloop()
