# Найти и вывести все гласные буквы (без повторений), которые встречаются в самом коротком слове.
# Текст запрашивается у пользователя. Алфавит использовать английский.

def eject_vowels(s):
    s_split = s.split()
    letters = []
    small_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    capital_vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    shortest_word = min(s_split)

    for o in range(len(shortest_word)):
        for c in range(len(capital_vowels)):
            if shortest_word[o] == capital_vowels[c]:
                letters.append(capital_vowels[c])
                capital_vowels[c] = ''

    for o in range(len(shortest_word)):
        for sm in range(len(small_vowels)):
            if shortest_word[o] == small_vowels[sm]:
                letters.append(small_vowels[sm])
                small_vowels[sm] = ''
    return letters


let = eject_vowels(input())
print(' '.join(let))


# альтернативное решение
def eject_vowels_alt(s):
    s_split = s.split()
    letters = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    shortest_word = min(s_split)

    for ind in range(len(shortest_word)):
        if shortest_word[ind] in vowels and shortest_word[ind] not in letters:
            letters.append(shortest_word[ind])
    return letters


st = eject_vowels_alt(input())
print(' '.join(st))
