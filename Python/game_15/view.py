from tkinter import *
from tkinter.ttk import Combobox
from tkinter.colorchooser import askcolor
from tkinter import font

def fontselection(combofont,spinfont,buttonfont):

    """ Функция позволяет выбрать шрифт надписи фишки"""
    
    familiesfont = font.families()
    combofont['values'] = familiesfont
    combofont['state'] = "readonly"
    combofont.current(0)  # установлен вариант по умолчанию  
    combofont.grid(column=4, row=0)
    combofont.bind("<<ComboboxSelected>>",
                    lambda e, f = combofont: checkcombo(e,f))  # обработка события выбора варианта    
    spinfont.grid(column=5, row=0)
    buttonfont.grid(column=6, row=0)   

def checkcombo(event,combofont):

    """ Выбор названия шрифта"""
    global namefont
    namefont = combofont.get()

def checkspin(spinfont):

    """ Выбор размера шрифта"""

    global sizefont
    sizefont = spinfont.get()

def checkbuttonfont(numrows,numcolumns,dimbtn,combofont,spinfont,buttonfont):

    """ Обработка кнопки выбора шрифта"""

    for x in range(numrows):
        for y in range(numcolumns):
            dimbtn[x][y]['font'] = (namefont, int(sizefont))
    combofont.grid_remove()
    spinfont.grid_remove()
    buttonfont.grid_remove()

def colorselection(numrows,numcolumns,dimbtn):
    
    """ Функция позволяет выбрать цвет фона фишки"""

    color = askcolor()[1]
    for x in range(numrows):
        for y in range(numcolumns):
            dimbtn[x][y]['bg'] = color
