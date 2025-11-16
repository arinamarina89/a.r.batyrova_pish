# Задача 1: уникальные слова
# Условие: Дана строка, содержащая несколько слов. Найдите все уникальные слова в строке и выведите их в алфавитном порядке.

sentence = "apple banana apple orange banana kiwi"

words = sentence.split()     # разбивка строки рна слова
unique_words = list(set(words))  # ток уникальные остаются 
unique_words.sort()          # сортировка

print(unique_words)
