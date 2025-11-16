# Задание 4: поиск подмассива с максимальной суммой
# Дан список целых чисел и длина подмассива k. Нужно найти подмассив длины k, сумма элементов которого будет максимальной.

array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 3

max_sum = None
best_subarray = None

for i in range(len(array) - k + 1):
    current = array[i:i + k]
    s = sum(current)

    if max_sum is None or s > max_sum:
        max_sum = s
        best_subarray = current

print("Подмассив с максимальной суммой:", best_subarray)
print("Сумма =", max_sum)
