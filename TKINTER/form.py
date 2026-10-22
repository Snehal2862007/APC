from tkinter import *
root=Tk()
root.title("Registration form")
root.geometry("500x500")
Label(root, text='Roll no:').pack()
roll=Entry(root)
roll.pack()
Label(root, text='Name:').pack()
name=Entry(root)
name.pack()
submit=Button(root,text="Submit")
submit.pack()
root.mainloop()





