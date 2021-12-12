# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

s = input()
first_h = s.find('h')
last_h = s.rfind('h')
r = s[:first_h+1]
t = s[first_h+1:last_h]
y = s[last_h:]
print(r + t.replace('h', 'H') + y)
