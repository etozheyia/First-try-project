# Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их
# в порядке возрастания.

a = set((input()).split())
b = set((input()).split())
ab = a & b
print(*sorted(ab, key=int))

# альтернативное решение
print(*sorted(set(input().split()) & set(input().split()), key=int))
