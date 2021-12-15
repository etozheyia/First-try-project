# Пользователь вводит строку и символ. В строке найти все вхождения этого символа и перевести его в верхний регистр,
# а также удалить часть строки, начиная с последнего вхождения этого символа и до конца.

s = input()
l = input()
small_a = ord('a')
capital_a = ord('A')
delta = small_a - capital_a
new_letter = ''

for i in range(len(s)):
    if s[i] == l:
        new_letter = chr(ord(l) - delta)
        s = s.replace(s[i], new_letter)
        break

print(s[0:s.rfind(new_letter)])
