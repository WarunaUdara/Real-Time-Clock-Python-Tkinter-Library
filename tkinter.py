from tkinter import *
import time

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    lbl1.config(text=current_time)
    window.after(1000, update_time)

window = Tk()
window.title("Real-Time Time Display")
window.geometry("500x500")

lbl1 = Label(window, text="", font=("calibri", 30))
lbl1.pack()

update_time()  #invoke time updating function 

window.mainloop()
