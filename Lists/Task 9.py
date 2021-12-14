# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

a = [int(i) for i in input().split()]
max_el = max(a)
min_el = min(a)
for i in range(len(a)):
    if a[i] == max_el:
        a[i] = min_el
    elif a[i] == min_el:
        a[i] = max_el
print(' '.join([str(i) for i in a]))
