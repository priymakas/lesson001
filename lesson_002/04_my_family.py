
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Алина", "Максим", "Аня"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [["Алина", 168], ['Максим', 80], ["Аня", 100]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
Son_height=my_family_height[1][1]
print("Son height " + "- " + str(Son_height) + " cm")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
family_height=(my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1])
print("Total height of family - " + str(family_height) + " cm")
