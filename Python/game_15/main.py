from tkinter import *
from logic import *
from menu import *

"""
    Программа игра в 15
    file.py -  функции сохранения/чтения позиции из файла и генерации
        случайной позиции
    logic.py  - функция обработка клика мышью на фишку
    menu.py - функция строит структуру меню программы    
    view.py - функции выбора и настройки шрифтов и цвета кнопок
"""

if __name__ == '__main__':

    # Открываем окно приложения

    window = Tk()
    window.title("Игра 15")
    window.geometry('800x650')

    numrows = 4
    numcolumns = 4
    indbut = 1
    dimbtn = [[0 for x in range(numrows)] for x in range(numcolumns)]
    # Заполнение массива фишек-кнопок
    for x in range(numrows):
        for y in range(numcolumns):
            dimbtn[x][y] = Button(window, text=str(indbut), font=("Arial", 50),
                                  height=1, width=3,
                                  command = lambda x1 = x, y1 = y: 
                                  color_change(x1,y1,numrows,numcolumns,dimbtn))
            dimbtn[x][y].grid(column=y, row=x)
            indbut = indbut + 1

    dimbtn[3][3].config(text = "  ") # Свободное место

    menu(numrows,numcolumns,dimbtn,window)

    window.mainloop()
