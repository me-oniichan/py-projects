from tkinter import *
import random


choice_list = ['scissor','stone','paper']
root = Tk()
Label(root, text = "START", fg = "red", font ="Arial 20 bold").pack(pady = 3)

result = StringVar()
result.set("about to begin")

l1 = Label(root,textvariable = result)
l1.pack(side = "bottom", anchor = 'center')


user = IntVar()
comp = IntVar()
user.set(0)
comp.set(0)

def game(r):
    global user, comp, result, choice_list, userp, compp
    ch = random.choice(choice_list)
    print(r)
    if ch == r:
        result.set(f'Draw, both choose ,{ch}')
        
    elif ch =='scissor' and r =='stone':
        result.set(f'You won, computer choose {ch}')
        user.set(user.get()+1)

    elif ch =='scissor' and r=='paper':
        result.set(f'You lost, computer choose {ch}')
        comp.set(comp.get()+1)

    elif ch =='stone' and r=='scissor':
        result.set(f'You lost, computer choose {ch}')
        comp.set(comp.get()+1)

    elif ch =='stone' and r=='paper':
        result.set(f'You won, computer choose {ch}')
        user.set(user.get() + 1)

    elif ch =='paper' and r=='stone':
        result.set(f'You lost, computer choose {ch}')
        comp.set(comp.get()+1)

    elif ch =='paper' and r =='scissor':
        result.set(f'You won, computer choose {ch}')
        user.set(user.get()+1)
    root.update()
    userp.update()
    compp.update()


root.geometry('400x300')
root.title('stone paper scissor')


f3=Frame(root)
scissor = Button(f3, text = 'Scissor',command = lambda : game("scissor"))
scissor.pack(side=LEFT,anchor='n', padx = 3)

paper = Button(f3, text = 'Paper',command = lambda : game("paper"))
paper.pack(side=LEFT,anchor='n', padx = 3)

stone = Button(f3, text = 'Stone',command = lambda : game("stone"))
stone.pack(side=LEFT, anchor='n', padx = 3)
f3.pack()

score = Label(root,text='Score', font='Lucida 15 bold').pack(anchor='center')

def result_disp():
    if user.get()>comp.get():
        hist.insert(0,f'You won by {user.get()-comp.get()} points')

    elif user.get()==comp.get():
        hist.insert(0,'Match was DRAW')

    else:
        hist.insert(0,f'computer won by {comp.get()-user.get()} points')
    user.set(0)
    comp.set(0)

f2=Frame(root)
you=Label(f2, text='You', font='Lucida 15 underline bold', fg ="green").pack(side=LEFT, padx=9)
comp_=Label(f2, text='COMP', font='Lucida 15 underline bold', fg = "blue").pack(side=RIGHT, padx=9)
userp=Label(f2, textvariable = user, font='Lucida 14 bold')
userp.pack(side=LEFT, anchor = 'sw')
compp=Label(f2, textvariable = comp, font='Lucida 14 bold')
compp.pack(anchor='se', side = RIGHT)
f2.pack(anchor='center')



scr=Frame(root)
scr.pack()
sc=Scrollbar(scr)
sc.pack(side=RIGHT, fill=Y)

hist=Listbox(scr, yscrollcommand=sc,width=25,relief=FLAT, height=7)
hist.pack(side=LEFT,pady=4)
sc.config(command=hist.yview)

bt=Button(root, text = 'Declare', command = result_disp).pack(side = BOTTOM, padx=10, pady=3)
root.mainloop()
