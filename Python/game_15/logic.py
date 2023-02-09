def fontcolor(numrows,numcolumns,dimbtn):
    
    """ Установка цвета текста всех фишек в системный цвет """

    for x in range(numrows):
        for y in range(numcolumns):
            dimbtn[x][y]['fg'] = 'SystemButtonText'

def color_change(x,y,numrows,numcolumns,dimbtn):
    
    """ Обработка клика мышью на фишку """
    
    fontcolor(numrows,numcolumns,dimbtn)
    # Lxy - список списков возможных ходов кликнутой фишкой
    Lxy = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for item in Lxy: # Цикл по возможный ходам
        xL = x + item[0]
        yL = y + item[1]
        flag = True
        # Проверка, возможен ли ход кликнутой фишкой. Ограничение по границам поля.
        if (xL < numrows) and (xL >= 0) and (yL < numcolumns) and  (yL >= 0):
            # Проверка, возможен ли ход кликнутой фишкой. Ограничение по свободному месту.
            if (dimbtn[xL][yL]['text'] == "  "):
                dimbtn[xL][yL]['text'] = dimbtn[x][y]['text']
                dimbtn[x][y]['text'] = "  "
                flag = False # Ход фишкой сделан
                break # Выход из цикла по свободным ходам                  
    if flag: dimbtn[x][y].config(fg="red") # У этой фишки хода нет
