from tkinter import *
from tkinter import ttk
import string as st
import math as meth
lxy = {'A': '0 0', 'B': '1 0', 'C': '2 0', 'D': '3 0', 'E': '4 0', 'F': '5 0', 'G': '6 0', 'H': '0 1', 'I': '1 1', 'J': '2 1', 'K': '3 1', 'L': '4 1', 'M': '5 1', 'N': '6 1', 'O': '0 2', 'P': '1 2', 'Q': '2 2', 'R': '3 2', 'S': '4 2', 'T': '5 2', 'U': '6 2', 'V': '1 3', 'W': '2 3', 'X': '3 3', 'Y': '4 3', 'Z': '5 3'}

def start_up():
    global root
    root = Tk()
    root.title("Hangman Game | Toshi")
    root.geometry("900x500")

def start_button():
    if v.get() == 'Select Difficulty': ddm.config(fg='red')
    else: game_loop()


def start_menu():
    global v
    global ddm
    canvas = Canvas(root, width=900, height=100)
    canvas.create_text(450,
                    50,
                    text="Hangman",
                    fill="black",
                    font=('Helvetica 15 bold'))

    dif_menu = ["Easy", "Medium", "Hard", "Impossible"]
    v = StringVar()
    v.set("Select Difficulty")
    ddm = OptionMenu(root, v, *dif_menu)
    ddm.config(width=12, fg='black')
    sub_button = Button(root, text="Play!", command=start_button())
    canvas.pack()
    ddm.place(relx=0.5, rely=0.2, anchor= 'center')
    sub_button.place(relx=0.5, rely=0.3, anchor= 'center')

def game_loop():
    global i
    for i in st.ascii_uppercase:
        i = abc_buttons(i)
        i.post_buttons()
        



class abc_buttons:
    def __init__(self, letter):
        self.letter = letter
        self.pos = lxy[letter]

    def post_buttons(self):
        self.letter_button = Button(root, text=self.letter, command=((self.letter).press())).grid(row=self.pos[0],column=self.pos[2])
        self.letter_button.place(relx=0.5, rely=0.3, anchor= 'center')
    def press(self):

start_up()
start_menu()
root.mainloop()