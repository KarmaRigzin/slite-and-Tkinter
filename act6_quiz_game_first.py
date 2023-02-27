from tkinter import *

def second():
    root.destroy()
    import act6_quiz_game_second
    second.quiz()

root=Tk()
root.geometry('300x200')

Label(root, text="Welcome to Quiz Game",font=("Arial", 14, "bold"),fg="blue").pack(pady =10)

Button(root, text="Start",font=("Arial", 12, "bold"),fg="red", command=second).pack(pady =10)

Button(root, text="Exit",font=("times new roman",10,"bold"),fg = "green", command=root.destroy).pack(pady =10)


root.mainloop()
