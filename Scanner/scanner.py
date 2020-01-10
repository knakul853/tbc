from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog

# from PIL import Image, ImageTk
import sys

# Root Setup
root = tk.Tk()
text = tk.Text(root)

# Function Setup for the model.
def main():
    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'),("Image File",'.png')])
    messagebox.showinfo("path", path)


# setting the minimun size of the root window
root.minsize(600, 800)
# Background Color of the window
root.configure(background='#242F3E')

myFont = Font(family="Times New Roman", size=12,)
text.configure(font=myFont)


myFont.configure(size=30)


root.title('Scanner')

img = PhotoImage(file='../image/barcode.png')
root.tk.call('wm', 'iconphoto', root._w, img)

style = ttk.Style()
style.theme_use('clam')

photo = PhotoImage(file='../image/barcode.png').subsample(40, 40)

# Display the summarized result
MyButton1 = ttk.Button(root, text='Scanner', width=20, command=main)
MyButton1.grid(row=15, column=0,padx=10,pady=10)
btn2 = tk.StringVar()



root.wm_attributes('-topmost', 1)
btn2.set('google')
root.mainloop()