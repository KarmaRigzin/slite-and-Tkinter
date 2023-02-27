from tkinter import *

def end(s):
    def quit_quiz():
        root.destroy()
        
    root=Tk()
    root.geometry('250x250')

    Label(root, text="Thank you for playing",font = ("calibri",13,"bold"),fg ="blue").pack()

    game_label=Label(root, text="")
    game_label.pack()
    game_label.config(text=f"Game Over! Your score is {s}",font = ("calibri",13,"bold"),fg ="blue")

    Button(root, text="Quit", command=root.destroy).pack()

    root.mainloop()
