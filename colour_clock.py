from tkinter import *
import time
import random

def update_time():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time, fg=random.choice(colors))
    label.after(1000, update_time)

root = Tk()
root.title("Colorful Clock")
label = Label(root, font=("Arial", 50), bg="black")
label.pack()
update_time()
root.mainloop()