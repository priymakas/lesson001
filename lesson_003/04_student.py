# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
count_months = 0
first_month = expenses - educational_grant
result = [first_month]
while expenses < (expenses + expenses * 0.03):
    expenses = expenses + expenses * 0.03
    balance = expenses - educational_grant
    result.append(balance)
    count_months += 1
    if count_months >= 9:
        print("Студенту надо попросить "+ str(round(sum(result),2)) + " рублей")
        break