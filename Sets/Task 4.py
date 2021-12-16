# Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите
# слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

a = [int(i) for i in input().split()]
b = set(a)

for i in a:
    if i in b:
        b.discard(i)
        print('NO')
    else:
        print('YES')