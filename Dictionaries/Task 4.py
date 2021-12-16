# Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте
# встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

dictionary = dict()
for i in range(int(input())):
    row = input().split()
    for word in row:
        dictionary[word] = dictionary.get(word, 0) + 1

max_value = max(dictionary.values())
frequent_word = [key for key, val in dictionary.items() if val == max_value]
print(min(frequent_word))
