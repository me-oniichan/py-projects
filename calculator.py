from tkinter import *
from math import *
root=Tk()
root.geometry('300x400')
root.title('My Calculator')
root.config(background='#212121')

def value(n):
    val.set(val.get() + n)
    screen.focus_set()
    screen.icursor("end")

def clear():
    val.set('')
    screen.focus_set()
    screen.icursor("end")
def result():
    try:
        cal=eval(val.get())
        val.set(cal)
        screen.focus_set()
        screen.icursor("end")
    except:
        val.set('error')

l1=Label(root, text='Calculator',fg='white',bg='#313131',font='lucida 18 bold')
l1.pack()
val=StringVar()
screen= Entry(root,text=val.get(),borderwidth=2,relief=SUNKEN,font='comic 14',width=300,textvariable=val, justify = "right")
screen.pack()

main = Frame(root,bg='#212121')
main.pack(pady = 5)


sub_f1= Frame(main,bg='#212121')
sub_f1.pack()

f1 = Frame(main,bg='#212121')
sub_f2 = Frame(f1)
child_f2_1 = Frame(sub_f2,bg='#212121')
child_f2_2 = Frame(sub_f2,bg='#212121')
child_f2_1.pack()
child_f2_2.pack()
f1.pack()
sub_f2.pack(side = "left")

f2 = Frame(main,bg='#212121')
sub_f3 = Frame(f2,bg='#212121')
child_f3_1 = Frame(sub_f3, bg='#212121')
child_f3_2 = Frame(sub_f3, bg='#212121')
child_f3_1.pack()
child_f3_2.pack()
sub_f3.pack(side = "left")
f2.pack()

#Buttons (operators)
b11= Button(sub_f1, text='C',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=clear).pack(side='left',padx=3,pady=3)
b22= Button(f1, text='+',fg='#a1a1a1',bg='#414141',height = 5, width = 4,font='comic 13',command=lambda : value("+")).pack(side='right',pady=3)
b33= Button(sub_f1, text='-',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("-")).pack(side='left',padx=3,pady=3)
b44= Button(sub_f1, text='*',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("*")).pack(side='left',padx=3,pady=3)
b55= Button(sub_f1, text='/',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("/")).pack(side='left',padx=3,pady=3)

#Buttons (Numbers)
b9= Button(child_f2_1, text='9',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("9")).pack(side='right',padx=3,pady=3)
b8= Button(child_f2_1, text='8',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("8")).pack(side='right',padx=3,pady=3)
b7= Button(child_f2_1, text='7',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("7")).pack(side='right',padx=3,pady=3)

b6= Button(child_f2_2, text='6',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("6")).pack(side='right',padx=3,pady=3)
b5= Button(child_f2_2, text='5',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("5")).pack(side='right',padx=3,pady=3)
b4= Button(child_f2_2, text='4',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("4")).pack(side='right',padx=3,pady=3)

b3= Button(child_f3_1, text='3',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("3")).pack(side='right',padx=3,pady=3)
b2= Button(child_f3_1, text='2',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("2")).pack(side='right',padx=3,pady=3)
b1= Button(child_f3_1, text='1',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value("1")).pack(side='right',padx=3,pady=3)

b0= Button(child_f3_2, text='0',fg='#a1a1a1',bg='#414141',height = 2, width = 10,font='comic 13',command=lambda : value("0")).pack(side='left',padx=3,pady=3)
b= Button(child_f3_2, text='.',fg='#a1a1a1',bg='#414141',height = 2, width = 4,font='comic 13',command=lambda : value(".")).pack(side='left',padx=3,pady=3)
#Buttons (result)
be= Button(f2, text='=',fg='#a1a1a1',bg='#414141',height = 5, width = 4,font='comic 13',command=result).pack(side='right',pady=3)


root.mainloop()