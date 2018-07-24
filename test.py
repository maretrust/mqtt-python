from Tkinter import *

root = Tk()

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes("-fullscreen", True) 



frame = Frame(root, name="saefy")


colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1


# w = Label(root, name="label1", text="red", bg="red", fg="white")
# w.pack(padx=5, pady=10, side=LEFT)
# w = Label(root, text="green",name="label2", bg="green", fg="black")
# w.pack(padx=5, pady=20, side=LEFT)
# w = Label(root, text="blue",name="label3", bg="blue", fg="white")
# w.pack(padx=5, pady=20, side=LEFT)

# lt = root.nametowidget(".label1")
# lt

root.mainloop()