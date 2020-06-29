import tkinter as tk
import time as tt
from tkinter import messagebox
master = tk.Tk()

show = tk.StringVar() 
brk = 0
time = 1
last =0

def count_wpm():
    global text, time, display, show, last, val, brk
    if brk < 3:
        a = tt.time()
        get = text.get(1.0, 'end-1c').split()
        number = len(get)

        if number == last:
            brk+=1
        else:
            brk = 0
        show.set(str(number*60/time)[:4])
        time+=1
        display.update()
        last = number
        b= tt.time() - a
        loop = master.after(int(1000- b*100), count_wpm)
    else:
        print("paused")
        val = 0
    
val = 0
def ext(event):
    global val, brk
    if brk == 3:
        brk = 0
    if val == 0:
        count_wpm()
    val = 1

def reset():
    global time, text, brk, show
    ask = messagebox.askyesno("CONFIRMATION", "Do you really wnt to reset")
    if ask == True:
        brk = 3
        time = 1
        text.delete(1.0, 'end')
        show.set("")

master.title('Type Master')

stat = tk.Frame(master, bg = "#565656", height = 18)
stat.pack(fill = "x", side = "bottom")


display = tk.Label(stat, textvariable = show, bg = "#565656", fg = "#efefef")
display.pack(side = "right", padx = 3, pady =2, ipadx = 3)

w = tk.Label(stat, text = "WPM : ", bg = "#565656", fg = "#efefef")
w.pack(side = "right", padx = 3, pady =2)


text= tk.Text(master, fg = '#141414', relief = tk.FLAT, borderwidth = 3, font = "Arial 12 ")
text.pack(fill = 'both', padx = 3)
text.bind("<Key>", ext)


re = tk.Button(stat, text = "Reset", bg  = "#131313", fg = "#efefef", command = reset)
re.pack(padx = 5, pady = 3, side = tk.LEFT)


master.mainloop()