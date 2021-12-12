# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

s = input()
n = len(s)
for i in range(n):
    if i % 3 == 0:
        s = s.replace(s[i], '*', 1)
print(s.replace('*', ''))
