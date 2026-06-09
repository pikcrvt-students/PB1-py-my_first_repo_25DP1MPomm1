from tkinter import *
logs = Tk()
logs.title('Citplanētietis')
a = Canvas(logs, height=300, width=300)
a.pack()
kermenis = a.create_oval(100, 150, 300, 250, fill='green')
acs = a.create_oval(170, 70, 230, 130, fill='white')
zilite = a.create_oval(190, 90, 210, 110, fill='black')
mute = a.create_oval(150, 220, 250, 240, fill='red')
kakls = a.create_line(200, 150, 200, 130)
cepure = a.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')

def mute_vala():
    a.itemconfig(mute, fill='black')


def mute_ciet():
    a.itemconfig(mute, fill='red')


def mirkskinat():
    a.itemconfig(acs, fill='green')
    a.itemconfig(zilite, state=HIDDEN)


def nemirkskinat():
    a.itemconfig(acs, fill='white')
    a.itemconfig(zilite, state=NORMAL)


vardi = a.create_text(200, 280, text='Es esmu citplanētietis!')

def zagt_cepuri():
    a.itemconfig(cepure, state=HIDDEN)
    a.itemconfig(vardi, text='Atdod manu cepuri!')


logs.attributes('-topmost', 1)

def zagas(notikums):
    mute_vala()
    a.itemconfig(vardi, text='Ik!')


a.bind_all('<Button>-1', zagas)

def mirkskinat2(notikums):
    a.itemconfig(acs, fill='green')
    a.itemconfig(zilite, state=HIDDEN)


def nemirkskinat2(notikums):
    a.itemconfig(acs, fill='white')
    a.itemconfig(zilite, state=NORMAL)


a.bind_all('<KeyPress-a>', mirkskinat2)
a.bind_all('<KeyPress-z>', nemirkskinat2)

def acs_vadiba(notikums): 
    taustins = notikums.keysym
    if taustins == 'Up' :
        a.move(zilite, 0, -1)
    elif taustins == 'Down' :
        a.move(zilite, 0, 1)
    elif taustins == 'Left' :
        a.move(zilite, -1, 0)
    elif taustins == 'Right' :
        a.move(zilite, 1, 0)


a.bind_all('<Key>', acs_vadiba)
    
logs.mainloop()
