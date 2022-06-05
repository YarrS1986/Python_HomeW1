# Сформировать список из N членов последовательности
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = int(input("Введи число N = "))
array = range(N)

for i in array:
    if i % 2:
        print(-3 ** i)
    else:
        print(3 ** i)
