# Задание 1: Описание функции

def f(x):
    if x < -2:
        return 4
    elif -2 <= x < 2:
        return x ** 2
    else:  # x >= 2
        return x ** 2 + 4 * x + 5


# применение
x = float(input("Введите x: "))
print("f(x) =", f(x))