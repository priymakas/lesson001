# -*- coding: utf-8 -*-
5
# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
# user_input = input("Введите, пожалуйста, номер месяца: ")
# month = user_input
user_input= []
while user_input == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12":
    user_input = input("Введите, пожалуйста, номер месяца: ")
    if user_input == "1":
        print('Вы ввели', " 31 day", user_input)
        break
    elif user_input == "2":
        print('Вы ввели', user_input, " 28 day")
        break
    elif user_input == "3":
        print('Вы ввели', user_input, " 31 day")
        break
    elif user_input == "4":
        print('Вы ввели', user_input, " 30 day")
        break
    elif user_input == "5":
        print('Вы ввели', user_input, " 31 day")
        break
    elif user_input == "6":
        print('Вы ввели', user_input, " 30 day")
        break
    elif user_input == "7":
        print('Вы ввели', user_input, " 31 day")
        break
    elif user_input == "8":
        print('Вы ввели', user_input, " 31 day")
        break
    elif user_input == "9":
        print('Вы ввели', user_input, " 30 day")
        break
    elif user_input == "10":
        print('Вы ввели', user_input, " 31 day")
        break
    elif user_input == "11":
        print('Вы ввели', user_input, " 30 day")
        break
    elif user_input == "12":
        print('Вы ввели', user_input, " 31 day")
        break
    else:
        print("Вы ввели некорректный номер месяца")
        continue
print("thank")

    # TODO здесь ваш код
