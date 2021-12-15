# Преобразовать список так, чтобы сначала шли все отрицательные элементы, а потом положительные(0 считать положительным)
# Порядок следования должен быть сохранен.

li = [int(i) for i in input().split()]
arrange = []

for o in li:
    if o < 0:
        arrange.append(o)

for i in li:
    if i >= 0:
        arrange.append(i)

print(' '.join([str(a) for a in arrange]))


# альтернативное решение
li = [int(i) for i in input().split()]
minus = []
plus = []

for el in li:
    if el < 0:
        minus.append(el)
    else:
        plus.append(el)

print(' '.join([str(a) for a in minus + plus]))
