import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def main():
    conn = sqlite3.connect('bmi.db')
    cur = conn.cursor()

    
    cur.execute('''CREATE TABLE IF NOT EXISTS bmi
         (Std_Code TEXT PRIMARY KEY,
         Name TEXT NOT NULL,
         Weight REAL NOT NULL,
         Height REAL NOT NULL,
         BMI REAL NOT NULL,
         Category TEXT NOT NULL DEFAULT 'Unknown')''')


    conn.commit()
    root = Tk()
    root.title("BMI Calculator")
    
    root.geometry('300x400')
    Label(root, text = "Student BMI Calculator",font=("times new roman",15)).grid(row = 0,column = 1)

    #variables
    code = StringVar()
    name = StringVar()
    weight = DoubleVar()
    height = DoubleVar()
    bmi = DoubleVar()
    category = StringVar()

    code_label = Label(root, text="Std Code").grid(row=1, column=0)
    code_entry = Entry(root,textvariable =code)
    code_entry.grid(row=1, column=1)

    name_label = Label(root, text="Name").grid(row=2, column=0)
    name_entry = Entry(root,textvariable =name)
    name_entry.grid(row=2, column=1)

    weight_label = Label(root, text="Weight-(kg)").grid(row=3, column=0)
    weight_entry = Entry(root,textvariable =weight)
    weight_entry.grid(row=3, column=1)

    height_label = Label(root, text="Height-(m)").grid(row=4, column=0)
    height_entry = Entry(root,textvariable =height)
    height_entry.grid(row=4, column=1)

    bmi_label = Label(root, text="BMI").grid(row=5, column=0)
    bmi_display = Label(root, text="",textvariable =bmi)
    bmi_display.grid(row=5, column=1)

    cat_label = Label(root, text="Category").grid(row=6, column=0)
    cat_display = Label(root, text="",textvariable =category)
    cat_display.grid(row=6, column=1)

    def calculate_bmi():
        w = float(weight_entry.get())
        h = float(height_entry.get())
        bmi_value = w / (h * h)
        bmi_display.config(text=str(round(bmi_value, 2)))
        if bmi_value <=18.5:
            category.set("Under Weight")
        elif bmi_value <= 25:
            category.set("Healthy")
        elif bmi_value <=30:
            category.set("Over weight")
        else:
            category.set("Obese")
        bmi.set(round(bmi_value, 2))

    calculate_button = Button(root, text="Calculate", command=calculate_bmi)
    calculate_button.grid(row=7, column=1)

    def addinfo():
        code_entry_value = code_entry.get()
        name_entry_value = name_entry.get()
        weight_entry_value = float(weight_entry.get())
        height_entry_value = float(height_entry.get())
        bmi_display_value = float(bmi_display.cget("text"))

        conn = sqlite3.connect('bmi.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO bmi (Std_Code, Name, Weight, Height, BMI, Category) VALUES (?, ?, ?, ?, ?, ?)", (code_entry_value, name_entry_value, weight_entry_value, height_entry_value, bmi_display_value, category.get()))

        conn.commit()
        conn.close()

        code_entry.delete(0, END)
        name_entry.delete(0, END)
        weight_entry.delete(0, END)
        height_entry.delete(0, END)
        bmi_display.config(text="")

        messagebox.showinfo("Success","Data added successfully")

    

    add_button = Button(root, text="Add Details",command=addinfo)
    add_button.grid(row=8, column=1)


    def display_data():
        conn = sqlite3.connect('bmi.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bmi")
        #c.execute("SELECT Std_Code, Name, Weight, Height, BMI, Category FROM bmi")

        data = c.fetchall()

        data_window = Toplevel(root)
        data_window.title("BMI Data")

        tree = ttk.Treeview(data_window, columns=("Std_Code","Name", "Weight", "Height", "BMI","Category"), show="headings")
        tree.heading("Std_Code", text="Std Code")
        tree.heading("Name", text="Name")
        tree.heading("Weight", text="Weight")
        tree.heading("Height", text="Height")
        tree.heading("BMI", text="BMI")
        tree.heading("Category", text="Category")
        tree.pack()

        for row in data:
            
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5],))

        conn.close()

    dis_button = Button(root, text="Display Data", command=display_data)
    dis_button.grid(row=9, column=1)


    def del_data():
    
        conn = sqlite3.connect('bmi.db')
        c = conn.cursor()

        c.execute("DELETE FROM bmi")

        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Data deleted successfully")

    del_button = Button(root, text="Delete Data", command=del_data)
    del_button.grid(row=10, column=1)

main()
