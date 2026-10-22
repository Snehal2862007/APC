from tkinter import *
root = Tk()
root.title("entry Widgets")
root.geometry("400x550")
Label(root, text="Enter Name:").pack()
name = Entry(root)
name.pack(pady=5)
root.mainloop()