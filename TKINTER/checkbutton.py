from tkinter import *
root = Tk()
root.title("checkbutton Widgets")
root.geometry("400x550")
agree = IntVar()
Checkbutton(root, text="I agree to the terms",
            variable=agree).pack(pady=5)
root.mainloop()
