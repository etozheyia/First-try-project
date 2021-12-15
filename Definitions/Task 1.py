# Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, меняя
# первую букву на большую.
# Например, print(capitalize('word')) должно печатать слово Word.
# На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв.
# Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы.
# При этом используйте вашу функцию capitalize().
# Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII. И функция chr(),
# которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.

def capitalize():
    s_split = s.split()
    string_s = ''
    small_a = ord('a')
    small_z = ord('z')
    capital_a = ord('A')
    delta = small_a - capital_a

    for z in s_split:
        if small_a <= ord(z[0]) <= small_z:
            capital_letter = chr(ord(z[0]) - delta)
            new_word = capital_letter + z[1:]
            string_s += (new_word + ' ')
    return string_s


s = input()
print(capitalize())


# Альтернативное решение 1

def capitalize_alt(s):
    return s.title()


st = input()
print(capitalize_alt(st))

# Альтернативное решение 2 (без использования функции)
string = input().title()
print(string)
