from tkinter.filedialog import *
import random

def loadposition(numrows,numcolumns,dimbtn):

    """ Функция читает из файла сохранённую позицию"""

    openfile = askopenfilename() # Выбрали файл позиции

    filepos = open(openfile, 'r') # Открыли файл позиции
    listposread = []
    listposread = eval(filepos.readline()) # Прочли и преобразовали список позиции
    filepos.flush()
    filepos.close()

# Меняем надписи и цвет на фишках
    indbut = 0
    for x in range(numrows):
        for y in range(numcolumns):
            dimbtn[x][y]['text'] = listposread[indbut][2]
            dimbtn[x][y]['fg'] = listposread[indbut][3]
            indbut = indbut + 1

def saveposition(numrows,numcolumns,dimbtn):

    """ Функция сохраняет в файле текущую позицию"""

    savefile = asksaveasfilename() # Выбрали директорию и имя файла сохранения позиции

# Формирование списка текущей позиции

    listposwrite = []
    for x in range(numrows):
        for y in range(numcolumns):
            listposwrite.append([x, y, dimbtn[x][y]['text'], dimbtn[x][y]['fg']]) 
    
# Запись файла позиции 

    filepos = open(savefile, 'w') # Открыли файл позиции
    filepos.write(str(listposwrite)) # Записали список позиции в файл
    filepos.flush()
    filepos.close()

def randomposition(numrows,numcolumns,dimbtn):

    """ Функция генерирует случайную позицию"""

# Генерируем последовательный список строк с
# номерами от 1 до 15 + свободное место
    listoriginal = []
    indbut = 1
    for item in range(numrows * numcolumns - 1):
        listoriginal.append(str(indbut))
        indbut = indbut + 1
    listoriginal.append('  ')

# Перемешиваем элементы listoriginal
    random.shuffle(listoriginal)

# Меняем надписи и цвет на фишках
    indbut = 0
    for x in range(numrows):
        for y in range(numcolumns):
            dimbtn[x][y]['text'] = listoriginal[indbut]
            dimbtn[x][y]['fg'] = 'SystemButtonText'
            indbut = indbut + 1
            
def exitprogram():
    print(exitprogram)
