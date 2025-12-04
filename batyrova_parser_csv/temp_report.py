# CSV : YEAR;MONTH;DAY;HOUR;MINUTE;TEMPERATURE

import argparse
import sys
from statistics import mean

def parse_args():
    parser = argparse.ArgumentParser(description="Отчёт по температуре.")
    parser.add_argument("-f", "--file", help="Имя CSV файла", required=True)
    parser.add_argument("-m", "--month", type=int, choices=range(1,13),
                        help="Статистика только для указанного месяца (1-12)")
    return parser.parse_args()

def parse_line(line):
    # удаляем пробелы и перенос строки
    parts = line.strip().split(";")

    # должно быть ровно 6 частей
    if len(parts) != 6:
        raise ValueError("Ожидалось 6 значений, разделённых ';'")

    # пробуем распарсить
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        hour = int(parts[3])
        minute = int(parts[4])
        temp = int(parts[5])
    except:
        raise ValueError("Невозможно преобразовать значения в числа")

    # проверки диапазонов
    if not (1 <= month <= 12):
        raise ValueError("Месяц должен быть от 1 до 12")
    if not (1 <= day <= 31):
        raise ValueError("День должен быть от 1 до 31")
    if not (0 <= hour <= 23):
        raise ValueError("Час должен быть от 0 до 23")
    if not (0 <= minute <= 59):
        raise ValueError("Минута должна быть от 0 до 59")
    if not (-99 <= temp <= 99):
        raise ValueError("Температура должна быть от -99 до 99")

    return year, month, day, hour, minute, temp

def process_file(filename):
    months = {i: [] for i in range(1, 13)}
    total = []
    errors = []

    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Файл не найден:", filename)
        sys.exit(1)

    with f:
        for idx, line in enumerate(f, start=1):
            if line.strip() == "":
                continue
            try:
                year, month, day, hour, minute, temp = parse_line(line)
                months[month].append(temp)
                total.append(temp)
            except ValueError as err:
                errors.append((idx, line.strip(), str(err)))

    return months, total, errors

def print_month_stats(month, temps):
    if len(temps) == 0:
        print(f"Месяц {month:02d}: данных нет")
    else:
        print(f"Месяц {month:02d}: средняя={mean(temps):.2f}, мин={min(temps)}, макс={max(temps)}")

def main():
    args = parse_args()
    months, total, errors = process_file(args.file)

    print("Чтение файла:", args.file)

    if errors:
        print("\nНайдены ошибки:")
        for idx, text, msg in errors:
            print(f"  Строка {idx}: {msg}. Текст: '{text}'")
        return

    print("\nСтатистика по месяцам:")
    if args.month:
        print_month_stats(args.month, months[args.month])
    else:
        for m in range(1, 13):
            print_month_stats(m, months[m])

    print("\nГодовая статистика:")
    if len(total) == 0:
        print("Нет данных")
    else:
        print("Среднегодовая =", round(mean(total), 2))
        print("Минимальная  =", min(total))
        print("Максимальная =", max(total))

if __name__ == "__main__":
    main()
