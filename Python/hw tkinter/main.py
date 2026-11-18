import tkinter as tk
from tkinter import messagebox


def show_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Enter a task!")
    else:
        result.config(text="Next Task: " + task)


def show_last(event):
    result.config(text="Last Character: " + entry.get()[-1])


def mouse_click(event):
    result.config(text="Routine area clicked!")


root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("300x250")


tk.Label(root, text="Enter Your Task").pack(pady=5)


entry = tk.Entry(root)
entry.pack()
entry.bind("<KeyRelease>", show_last)


routine = tk.Label(root, text="My Daily Routine", bg="lightblue", width=25, height=3)
routine.pack(pady=15)
routine.bind("<Button-1>", mouse_click)


tk.Button(root, text="Next Task", command=show_task).pack()


result = tk.Label(root, text="")
result.pack(pady=10)


root.mainloop()


