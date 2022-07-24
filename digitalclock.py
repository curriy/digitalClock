from tkinter import *
from tkinter.ttk import *
from time import strftime

main = Tk()
main.title('Python clock')

def clock():
    tick = strftime('%H:%M:%S')
    clock_label.config(text = tick)
    clock_label.after(1000, clock)

clock_label = Label(main, font=('times', 80), background='black', foreground='white')
clock_label.pack(anchor = 'center')

def date():
    ticking = strftime('%d.%m.%Y')
    date_label.config(text = ticking)
    date_label.after(1000, date)

date_label = Label(main, font=('times', 64), background='black', foreground='white')
date_label.pack(anchor='center')

def initialize():
    clock()
    date()
    mainloop()

if __name__ == '__main__':
    initialize()
