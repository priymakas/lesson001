# x = []
# while x == "4" or "5":
#    x = input("Угадай число  ___ ")
#    if x == "4":
#       print("Удача")
#       break
#    elif x == "5":
#       print("Умничка")
#       break
#    else:
#       print("Не-а")
# print("Ты ввела правильное число и это  " + x)


def user():

    """fff"""
    name = input("Enter name")
    age = input("Enter age")
    return name, age


result = user()
print(result)
