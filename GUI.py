import tkinter as tk
from tkinter import ttk

# crearte the window
window = tk.Tk()
window.title("Class Schedule")
window.geometry("800x600")

# create widgets
text = tk.Text(master = window)

text.pack

label = ttk.Label(master = window, text = "Hello, World!")
label.pack()
window.mainloop()