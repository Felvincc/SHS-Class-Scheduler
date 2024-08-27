import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Class Scheduler")
window.geometry("400x600")

def normal_font():

    return ("Helvetica", 12)

def title_font():

    return ("Helvetica", 16)

# Function to increment the level number
def increment_level():
    level_num.set(level_num.get() + 1)

# Function to decrement the level number
def decrement_level():
    if level_num.get() > 0:  # Ensure the level number doesn't go below 0
        level_num.set(level_num.get() - 1)


def start():

    ask_level = tk.Label(window, text="Add or Remove Levels", font = normal_font())
    ask_level.pack(padx=10, pady=10, anchor="w")

    frame = tk.Frame(window)

    global level_num
    level_num = tk.IntVar(value=1)

    

    add_button = ttk.Button(frame, text="+", width=5, command= increment_level)
    add_button.pack(side="left")
    remove_button = ttk.Button(frame, text="-", width=5, command= decrement_level)
    remove_button.pack(side="left")

    num_level_text = ttk.Label(frame, textvariable = level_num, font = normal_font())
    num_level_text.pack(side="right")
    frame.configure(bg="black")
    frame.pack(padx=10, pady=10, anchor="w")

    normal_level_num = level_num.get()

  
        


    window.mainloop()

start()