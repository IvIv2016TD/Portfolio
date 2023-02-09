#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)

class Vec2d(): # Класс 2-мерных векторов

    """
        Класс 2-мерных векторов.
        Начало вектора - (0,0), начало координат.
        Вектор задаётся координатами (x,y) конца. 
    """

    def __init__(self, *arg):

        if len(arg) == 0: # Пустой объект Vec2d
            pass
        else:
            self.x = arg[0]
            self.y = arg[1]
        pass

    def __add__(self, term): # Сумма векторов

        return Vec2d(self.x + term.x, self.y + term.y)
        pass

    def __sub__(self, subtrahend): # Разность векторов
        
        return Vec2d(self.x - subtrahend.x, self.y - subtrahend.y)
        pass

    def __mul__(self, const_number): # Произведение на число
        
        return Vec2d(self.x * const_number, self.y * const_number)        
        pass

    def len(self): # Длина вектора
        
        return int(round((math.sqrt(self.x * self.x + self.y * self.y)), 0))
        pass

    def int_pair(self): # Возвращает кортеж из 2 целых чисел
                        # (текущие координаты вектора)
        result = (int(self.x), int(self.y))
        return result
        pass
    
    def mirror_x(self): # Отражение точки от стенки x

        self.x = - self.x
        pass

    def mirror_y(self): # Отражение точки от стенки y

        self.y = - self.y
        pass    

    def __str__(self):

        return "Координата x = " + str(self.x) + \
               "  Координата y = " + str(self.y)


class Polyline(Vec2d): # Класс замкнутых ломаных

    """
        Класс ломанных кривых.
        Ломанная кривая описывается списком точек.
        Точка описывается списком двух объектов класса Vec2d:
        вектором координат и вектором скоростей
    """

    def __init__(self, *arg):
        super().__init__(*arg)

        self.list_point = []
        if len(arg) == 0: # Пустой объект Polyline
            pass
        else:
            self.list_point.append([arg[0], arg[1]])
        self.lengh = len(self.list_point)

        pass
    
# Начало методов итерирования объектов класса Polyline 

    def __getitem__(self, indx):
       
        if self.lengh == 0:
            return []
        elif abs(indx) < self.lengh:
            return self.list_point[indx]
        else:            
            raise IndexError
        pass

    def __iter__(self):

        self.index_iter = 0
        return self

    def __next__(self):

        if self.index_iter < 1:
            self.index_iter +=1
            return self[self.index_iter - 1]
        else:            
            raise StopIteration
        pass

# Конец методов итерирования объектов класса Polyline

    def append_(self, *arg): # Добавление новой точки в объект класса Polyline
                             # arg - кортеж двух объектов класса Vec2d
                             # орисывающих координаты и скорость точки

        self.list_point.append([arg[0], arg[1]])
        self.lengh = len(self.list_point)

        pass

    def extend_(self, *arg): # Добавление последовательности точек
                             # (arg - кортеж с объектом класса Polyline)
                             # к объекту Polyline

        for item in range(arg[0].lengh - 1):
            self.append_(arg[0][item][0], arg[0][item][1])
        self.lengh = len(self.list_point)

        pass

    def pop_(self): # Удаление последней точки в ломаной

        self.list_point.pop(self.lengh - 1)
        self.lengh = len(self.list_point)
        
        pass

    def fast(self, coeff_speed): # Увеличение скорости

        for item in self.list_point:
            item[1] = item[1] * coeff_speed
        
        pass

    def slow(self, coeff_speed): # Уменьшение скорости

        for item in self.list_point:
            ccc = 1. / coeff_speed
            item[1] = item[1] * ccc
        
        pass

# Начало методов сглаживания ломаной

    def get_point(self, alpha, deg=None): 

        if deg is None:
            deg = self.lengh - 1
        if deg == 0:
            return self.list_point[0][0]
        return (self.list_point[deg][0] * alpha) + \
                self.get_point(alpha, deg - 1) * (1 - alpha)
    
        pass

    def get_points(self, count):

        alpha = 1 / count
        #res = []
        res = Polyline()
        for i in range(count):
            res.append_(self.get_point(i * alpha), Vec2d(0, 0))
        return res
    
        pass

# Конец методов сглаживания ломаной

    def set_points(self): # Пересчёт координат точек
        
        for p in range(self.lengh):
            self.list_point[p][0] = self.list_point[p][0] + \
                                    self.list_point[p][1]
            if self.list_point[p][0].x > SCREEN_DIM[0] or \
               self.list_point[p][0].x < 0:
                self.list_point[p][1].mirror_x()
            if self.list_point[p][0].y > SCREEN_DIM[1] or \
               self.list_point[p][0].y < 0:
                self.list_point[p][1].mirror_y()

        pass

    def draw_points(self, param_pl,
                    style="points", width=3, color=(255, 255, 255)):

# Отрисовка ломаной

        font1 = pygame.font.SysFont("courier", 24)
        gameDisplay.blit(font1.render(
            param_pl, True, (128, 128, 255)), (10, 570))        

        if style == "line":
            for p_n in range(-1, self.lengh - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(self.list_point[p_n][0].x),
                                  int(self.list_point[p_n][0].y)),
                                 (int(self.list_point[p_n + 1][0].x),
                                  int(self.list_point[p_n + 1][0].y)), width)
        elif style == "points":
            #i = 0
            for p in self.list_point:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0].x), int(p[0].y)), width)

        pass

    def __str__(self):

        if self.lengh == 0: # Пустой объект Polyline
            return "Пустой объект Polyline"
        else:
            return str(self.list_point)
        
        pass


class Knot(Polyline): # Расчёт точек кривой по добавляемым «опорным» точкам

    """
        Класс сглаженных ломанных кривых.
    """

    def __init__(self, pl_arg, *arg):
        super().__init__(*arg)

        self.list_point = Polyline()
        if pl_arg.lengh == 0: # Пустой объект Polyline
            pass
        else:
            self.list_point = pl_arg
        self.lengh = pl_arg.lengh

        pass    

    def get_knot(self, count): # Метод сглаживания ломаной опорных точек  

        res_knot = Polyline()
        if self.lengh < 3:
            return Polyline()
        for i in range(-2, self.lengh - 2):
            ptn_knot = Polyline()

            ptn_knot.append_((self.list_point[i][0] +
                              self.list_point[i + 1][0]) * 0.5, 0)
            ptn_knot.append_(self.list_point[i + 1][0], 0)
            ptn_knot.append_((self.list_point[i + 1][0] +
                              self.list_point[i + 2][0]) * 0.5, 0)

            res_knot.extend_(ptn_knot.get_points(count))
         
        return res_knot  
        pass

class HelpScreen():

    def __init__(self, steps):
        
        self.data = []
        self.data.append(["F1", "Show Help"])
        self.data.append(["R", "Restart"])
        self.data.append(["P", "Pause/Play"])
        self.data.append(["Esc", "End of game"])
        self.data.append(["Num+", "More points"])
        self.data.append(["Num-", "Less points"])
        self.data.append(["D", "Deleting an anchor point"])
        self.data.append(["F", "Increasing the speed of the anchor points"])
        self.data.append(["S", "Decreasing the speed of the anchor points"])
        self.data.append(["Z-N", "Adding a polyline"])
        self.data.append(["E", "Deleting a driven polyline"])        
        self.data.append(["", ""])
        self.data.append([str(steps), "Current points"])

    def draw_help(self):

        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(self.data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================

"""
    К функциналу добавлено:
    - уменьшение количества опорных точек (d)
    - увеличение/уменьшение скорости опорных точек (f/s)
    - отрисовка нескольких ломаных (максимум 6)
      - добавление ломаной (z, x, c, v, b, n)
      - отмена управляемой ломаной (e) (ломаную z удалить нельзя)
      - отображение служебной информации:
        - имя ломаной
        - количество опорных точек
        - количество шагов сглаживания
"""

if __name__ == "__main__":

# Не понимая, что означает
# "вычислять длину вектора с использованием функции len(a)"
# реализовал методом
    l_vec_1 = Vec2d(1, 1).len()
    l_vec_2 = Vec2d(2, 2).len()

    name_polyline = [pygame.K_z, pygame.K_x, pygame.K_c,
                     pygame.K_v, pygame.K_b, pygame.K_n]

    dict_polyline = {} # В этом словаре храним словари с ключами -
                       # именами ломаных, значение - словари с
                       # ломаными и их параметрами

    steps = 35
    working = True
    coeff_speed_fast = 1.0
    coeff_speed_slow = 1.0
    show_help = False
    pause = True

    key_pl_z = 122 # Ключ неудаляемой ломаной
    spacepolyline = {} # Словари с ломаными и их параметрами
    spacepolyline["polyline"] = Polyline()
    spacepolyline["steps"] = steps
    spacepolyline["csf"] = coeff_speed_fast
    spacepolyline["css"] = coeff_speed_slow
    spacepolyline["pause"] = True
    dict_polyline[key_pl_z] = spacepolyline
    dp = dict_polyline[key_pl_z]
    key_pl = key_pl_z
    
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("Второе задание второй недели")

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_F1:
                    show_help = not show_help                    
                if event.key in name_polyline:
                    key_pl = event.key # Ключ ломаной
                    if event.key not in dict_polyline: # Новая ломаная
                        spacepolyline = {}
                        spacepolyline["polyline"] = Polyline()
                        spacepolyline["steps"] = steps
                        spacepolyline["csf"] = coeff_speed_fast
                        spacepolyline["css"] = coeff_speed_slow
                        spacepolyline["pause"] = True                        
                        dict_polyline[event.key] = spacepolyline
                dp = dict_polyline[key_pl]
                if event.key == pygame.K_r:
                    dp["polyline"] = Polyline()
                if event.key == pygame.K_p:
                    dp["pause"] = not dp["pause"]
                    pause = dp["pause"]
                if event.key == pygame.K_KP_PLUS:
                    dp["steps"] += 1
                if event.key == pygame.K_KP_MINUS:
                    dp["steps"] -= 1 if dp["steps"] > 1 else 0
                if event.key == pygame.K_d: # Удаление опорной точки,
                                            # введённой последней
                    dp["polyline"].pop_() if dp["polyline"].lengh > 0 else 0
                if event.key == pygame.K_f: # Увеличение скорости 
                                            # опорных точек в 1,2 раза
                    dp["csf"] = dp["csf"] * 1.2
                    dp["polyline"].fast(dp["csf"])
                if event.key == pygame.K_s: # Уменьшение скорости 
                                            # опорных точек в 1,2 раза
                    dp["css"] = dp["css"] * 1.2
                    dp["polyline"].slow(dp["css"])
                if event.key == pygame.K_e: # Удаление управляемой ломаной 
                                            
                    if key_pl != key_pl_z:
                        dict_polyline.pop(key_pl)
                        dp = dict_polyline[key_pl_z]
                        key_pl = key_pl_z # Вернулись к ломаной z
            if event.type == pygame.MOUSEBUTTONDOWN:
                dp["polyline"].append_(
                            Vec2d(event.pos[0], event.pos[1]),
                            Vec2d(random.random() * 2, random.random() * 2))
                
        gameDisplay.fill((100, 50, 200))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        for key in dict_polyline:
            pl = dict_polyline[key]["polyline"]
            param_pl = "Имя ломаной " + \
                       chr(key_pl) + \
                       " Опорных точек " + \
                       str(dp["polyline"].lengh) + \
                       " Шагов сглаживания " + \
                       str(dp["steps"])
            pl.draw_points(param_pl)       
            pl_knot = Knot(pl).get_knot(dict_polyline[key]["steps"])
            pl_knot.draw_points(param_pl, "line", 3, color)
            if not dict_polyline[key]["pause"]:
                pl.set_points()
            if show_help:
                HelpScreen(dp["steps"]).draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
