#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set = garden()
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
print(garden_set)
meadow_set = set(meadow)
print(meadow_set)
# выведите на консоль все виды цветов
# TODO здесь ваш код
all_flowers=garden + meadow
print(set(all_flowers))
print(garden_set.union(meadow_set))
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
print(garden_set.intersection(meadow_set))
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
print(garden_set.difference(meadow_set))
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
print(meadow_set.difference(garden_set))


