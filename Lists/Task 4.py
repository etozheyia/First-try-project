# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов
# одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.

a = [int(i) for i in input().split()]
count_p, count_m = 0, 0
for i in range(len(a)):
    if a[i] > 0:
        count_p += 1
        count_m = 0
        if count_p == 2:
            print(a[i - 1], a[i])
            break
    elif a[i] < 0:
        count_m += 1
        count_p = 0
        if count_m == 2:
            print(a[i - 1], a[i])
            break
