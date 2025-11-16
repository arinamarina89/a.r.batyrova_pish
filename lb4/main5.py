# Задача 5: анаграммы
# Условие: Даны две строки. Необходимо определить, являются ли они анаграммами (содержат одинаковые символы с одинаковой частотой).

string1 = "listen"
string2 = "silent"

# подсчет частоты символов вручную

def count_chars(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

freq1 = count_chars(string1)
freq2 = count_chars(string2)

print(freq1 == freq2)
