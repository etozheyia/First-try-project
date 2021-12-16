# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны.
#
# Для слова из словаря, записанного в последней строке, определите его синоним.

dictionary = {}
for i in range(int(input())):
    row = input().split()
    dictionary[row[0]] = row[1]

word = input()
if word in dictionary:
    print(dictionary[word])
else:
    [print(key) for key, value in dictionary.items() if word == value]


# альтернативное решение
n = int(input())
d = {}

for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first

print(d[input()])
