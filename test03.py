from tkinter import *
import tkinter
import tkinter.filedialog as filedialog
#? import

root = tkinter.Tk()
root.geometry('750x500')
root.resizable(width=False, height=False)
root.title(string='InClass Connector to DB')
#? root.info

var = StringVar()
label = Label(root, text='Groups:').pack(side=LEFT)
entry = Entry(root, textvariable=var).pack(side=LEFT)
button = Button(root, text='Browse', command=lambda:var.set(filedialog.askopenfilename())).pack(side=LEFT)

b = Button(root, text='ptint').pack(side=TOP)
b.bind('<Button-1>', print(entry))

root.mainloop()