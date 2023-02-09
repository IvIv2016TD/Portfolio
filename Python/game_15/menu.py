from tkinter import *
from file import *
from view import *

""" Функция строит структуру меню программы"""

def menu(numrows,numcolumns,dimbtn,window):
    # Строка меню 
    mainmenu = Menu(window)
    window.config(menu = mainmenu)

    filemenu = Menu(mainmenu, tearoff = 0)
    mainmenu.add_cascade(label = 'Файл', menu = filemenu)
    selectionpos = Menu(filemenu, tearoff = 0)
    filemenu.add_cascade(label = 'Выбор позиции', menu = selectionpos)
    selectionpos.add_command(label = 'Загрузить позицию', 
                            command = lambda: 
                            loadposition(numrows,numcolumns,dimbtn)) 
    selectionpos.add_command(label = 'Сохранить позицию как . . .', 
                            command = lambda: 
                            saveposition(numrows,numcolumns,dimbtn))
    selectionpos.add_command(label = 'Случайная позиция', 
                            command = lambda: 
                            randomposition(numrows,numcolumns,dimbtn))

    viewmenu = Menu(mainmenu, tearoff = 0)
    mainmenu.add_cascade(label = 'Вид', menu = viewmenu)
    view = Menu(viewmenu, tearoff = 0)
    viewmenu.add_command(label = 'Цвет', 
                        command = lambda: 
                        colorselection(numrows,numcolumns,dimbtn)) 
    viewmenu.add_command(label = 'Шрифт', 
                        command = lambda: 
                        fontselection(combofont,spinfont,buttonfont))

    combofont = Combobox(window)
    spinfont = Spinbox(window, from_= 8, to = 100, width = 5, 
                        command = lambda: checkspin(spinfont))
    buttonfont = Button(window, text = "Выбрать", 
                        command = lambda: 
                        checkbuttonfont(numrows,numcolumns,dimbtn,
                                        combofont,spinfont,buttonfont))
