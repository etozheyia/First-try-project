# Определите среднее значение всех элементов последовательности, завершающейся числом 0.

n = int(input())
amount = 0
summ = 0
while n != 0:
    amount += 1
    summ += n
    n = int(input())
print(summ / amount)
