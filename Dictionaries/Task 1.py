# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в
# этом тексте ранее.
#
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.

text = input().split()
words = {}

for key in text:
    if key not in words:
        words[key] = 0
        print(words[key], end=' ')
    else:
        words[key] += 1
        print(words[key], end=' ')


# альтернативное решение
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
