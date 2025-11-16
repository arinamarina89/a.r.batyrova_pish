# Задача 2: частота символов
# Условие: Дана строка, состоящая из символов. Необходимо подсчитать частоту каждого символа в строке и вывести её.

string = "abracadabra"

freq = {}

for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
