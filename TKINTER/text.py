from tkinter import *
root = Tk()
root.title("text Widgets")
root.geometry("400x550")
Label(root, text="Enter Address:").pack()
address = Text(root, height=3, width=30)
address.pack(pady=5)
root.mainloop()