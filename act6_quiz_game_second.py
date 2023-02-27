from tkinter import *
from tkinter import messagebox

score=0

def quiz():
    def end():
        global score
        root.destroy()
        import act6_quiz_game_third
        act6_quiz_game_third.end(score)

    def check1():
        global score
        if ans1.get()==4:
            score +=5
            score_label.config(text=f"Score: {score}")
            messagebox.showinfo("Correct", "Well done")
        else:
            score -=2
            score_label.config(text=f"Score: {score}")
            messagebox.showerror("Wrong", "Sorry")
            

    def check2():
        global score
        if ans2.get()==3:
            score +=5
            score_label.config(text=f"Score: {score}")
            messagebox.showinfo("Correct", "Well done")
        else:
            score -=2
            score_label.config(text=f"Score: {score}")
            messagebox.showerror("Wrong", "Sorry")


            
    def check4():
        global score
        if ans4.get()==2:
            score +=5
            score_label.config(text=f"Score: {score}")
            messagebox.showinfo("Correct", "Well done")
        else:
            score -=2
            score_label.config(text=f"Score: {score}")
            messagebox.showerror("Wrong", "Sorry")
                   
    root=Tk()
    root.geometry('500x600')

    ans = IntVar()
    ans1 =IntVar()
    ans2 =IntVar()
    ans3 =IntVar()
    ans4 =IntVar()

    Label(root, text="Quiz questions with possible answers",font=("times new roman",14,"bold"),fg="blue").pack()

    score_label=Label(root, text="Score: 0",font=("comic san",12,"bold"),fg="blue")
    score_label.pack()

  
    Label(root, text="What is the capital of Bhutan?").pack()
    
    Radiobutton(root, text="Trashigang", variable=ans1, value=1).pack()
    Radiobutton(root, text="Bumthang", variable=ans1, value=2).pack()
    Radiobutton(root, text="Punakha", variable=ans1, value=3).pack()
    Radiobutton(root, text="Thimphu", variable=ans1, value=4).pack()
    Button(root, text="Check", command=check1,font=("comic san",12,"bold"),fg="blue").pack()

    Label(root, text="What is largest country in the world?").pack()
    
    Radiobutton(root, text="China", variable=ans2, value=1).pack()
    Radiobutton(root, text="USA", variable=ans2, value=2).pack()
    Radiobutton(root, text="Russia", variable=ans2, value=3).pack()
    Radiobutton(root, text="Australia", variable=ans2, value=4).pack()
    Button(root, text="Check", command=check2,font=("comic san",12,"bold"),fg="blue").pack()


    Label(root, text="Who is world's richest man currently?").pack()
    
    Radiobutton(root, text="Elon", variable=ans4, value=1).pack()
    Radiobutton(root, text="Bernard", variable=ans4, value=2).pack()
    Radiobutton(root, text="Bezos", variable=ans4, value=3).pack()
    Radiobutton(root, text="Larry", variable=ans4, value=4).pack()
    Button(root, text="Check", command=check4,font=("comic san",12,"bold"),fg="blue").pack(pady =5)
    
    Button(root, text="Next", command=end,font=("comic san",12,"bold"),fg="blue").pack(pady = 5)


    root.mainloop()
quiz()
