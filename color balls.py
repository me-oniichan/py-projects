import tkinter as tk
import random as rn

draw = False
color = ["green", "red", "white", "black", "blue", "yellow", "gray", "brown", "orange","purple", "pink", "lightgreen", "lightblue"]

def animate(event):
    if draw:
        fill = rn.choice(color)
        obj =canvas.create_oval(event.x-7, event.y-7, event.x+7, event.y+7, fill=fill)   
        def move():
            canvas.move(obj, 0, 6)
            height = canvas.winfo_height()
            if canvas.coords(obj)[1] < height:
                root.after(10, move)
            else:
                canvas.delete(obj)
        move()

def trigger(bool):
    global draw
    draw = bool
    if draw:
        fill = rn.choice(color)
        x = root.winfo_pointerx() - root.winfo_rootx()
        y = root.winfo_pointery() - root.winfo_rooty()
        obj =canvas.create_oval(x-7, y-7, x+7, y+7, fill=fill)
        def move_single(): 
            canvas.move(obj, 0, 6)
            height = canvas.winfo_height()
            if canvas.coords(obj)[1] < height:
                root.after(10, move_single)
            else:
                canvas.delete(obj)
        move_single()  
        print(obj)


root = tk.Tk()
root.title("colorballs")
root.geometry("400x500")

canvas = tk.Canvas(root, bg = "black")
canvas.pack(fill = "both", expand = 1)

canvas.bind("<Button-1>", lambda x: trigger(True))
canvas.bind("<ButtonRelease-1>", lambda x: trigger(False))
canvas.bind("<B1-Motion>", animate)

root.mainloop()