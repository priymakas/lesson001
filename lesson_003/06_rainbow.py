# -*- coding: utf-8 -*-

# (цикл for)
import math

import pygame
import simple_draw as sd
point = sd.get_point(50, 100)
def line(point, color):
    width = 50
    for _ in range(3):
        sd.line(start_point=point, end_point=point, color=sd.COLOR_BLACK, width=4)

line(point=(50,100),color=sd.COLOR_BLACK)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
