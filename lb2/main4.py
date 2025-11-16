# Задание 4: Функция, определяющая сумму цифр числа

def sum_digits(n):
    n = abs(n)
    s = 0
    for digit in str(n):
        s += int(digit)
    return s


# применеение 
num = int(input("Введите число: "))
print("Сумма цифр числа:", sum_digits(num))
