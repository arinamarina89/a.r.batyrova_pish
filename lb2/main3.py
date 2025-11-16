# Задание 3: Определяет, верно ли, что сумма цифр числа равна произведению цифр

def sum_equal_product(n):
    n = abs(n)  # если число отрицательное
    s = 0
    p = 1
    for digit in str(n):
        s += int(digit)
        p *= int(digit)
    return s == p


# применение 
num = int(input("Введите число: "))
if sum_equal_product(num):
    print("Да, сумма цифр равна произведению")
else:
    print("Нет, сумма и произведение различаются")