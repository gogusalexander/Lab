def min_time_to_copy(n, x, y):
    # Если x больше y, меняем местами x и y для оптимизации (чтобы x было наименьшим)
    if x > y:
        x, y = y, x

    # Начнем бинарный поиск
    left = 0
    right = n * x

    while left < right:
        mid = (left + right) // 2

        # Время, за которое будут сделаны копии
        # Один ксерокс делает копии каждые x секунд, другой каждые y секунд
        copies = mid // x + mid // y

        if copies >= n:
            right = mid
        else:
            left = mid + 1

    return left


# Ввод данных
n, x, y = map(int, input().split())

# Вывод минимального времени
print(min_time_to_copy(n, x, y))