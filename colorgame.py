import tkinter as tk
import random as rn

clist = ['red', 'green', 'black', 'pink', 'yellow', 'purple', 'brown', 'blue', 'gray', 'orange']
namelist = ['red', 'green', 'black', 'pink', 'yellow', 'purple', 'brown', 'blue', 'gray', 'orange']

ct = True
def game(event):
    global color, flash, cdisplay, ans, score, ct
    if ct:
        time()
    if ans.get() == cdisplay.get():
        score.set(score.get()+1)
        sc.update()

    ans.set('')
    ctext = rn.choice(clist).upper()
    cdisplay.set(rn.choice(namelist))
    color.set(ctext)
    flash.config(fg = cdisplay.get())
    flash.update()
    answer.config(fg=cdisplay.get())
    answer.update()
    ct = False
sec = 20

tt = ''
def time():
    global sec, answer, sec, cdisplay, ct
    if sec > 0:
        sec-=1
        timer.set(str(sec))
        time_display.update()
    elif sec == 0:
        answer.config(state = 'disabled')
        timer.set("Time Up")
        cdisplay.set("black")
        color.set("Game Over")
        root.unbind("<Return>")
        answer.unbind("<Return>")
        ct = True
    root.after(1000, time)


root = tk.Tk()
root.geometry('600x400')
root.title('Color Game')
root.config(bg = '#2f2f2f')
root.bind('<Return>', game)

color = tk.StringVar()
color.set('Hit Enter to Start')
cdisplay = tk.StringVar()
cdisplay.set('black')
ans = tk.StringVar()
score = tk.IntVar()
score.set(0)
timer = tk.StringVar()
status = False

label_color= rn.choice(clist)



tk.Label(root, text = "Color Game", fg = label_color, bg = "#2f2f2f", font = "consolas 35 bold").pack(pady = 10)


flash = tk.Label(root, bg='#eeeeee', fg = cdisplay.get(), textvariable = color, font = 'consolas 30', borderwidth = 3, relief = tk.RIDGE, padx= 10, pady = 3)
flash.pack(padx = 10, pady= 8)

answer = tk.Entry(root, width=30,font= 'arial 15', textvariable = ans, fg= cdisplay.get())
answer.bind('<Return>', game)
answer.pack(side = 'bottom', padx = 4, pady = 20)

scframe = tk.Frame(root, bg = '#2f2f2f', width = 50, height = 20)
scframe.pack(padx = 20 , pady = 6)

lsc = tk.Label(scframe, text='score : ', bg = '#2f2f2f', font='time 25', fg = '#a1a1a1')
lsc.pack(side = tk.LEFT)
sc = tk.Label(scframe,textvariable = score, bg = '#2f2f2f', font='time 25',fg = '#a1a1a1')
sc.pack(side = tk.RIGHT)

time_display = tk.Label(root, textvariable = timer, font = 'time 18', bg = '#2f2f2f',fg = '#a1a1a1')
time_display.pack(padx = 5, pady = 5)

re = tk.Label(root, text = f'''Color List
{clist}''', fg = "#dfdfdf", bg = "#2f2f2f")
re.pack()
root.mainloop()
