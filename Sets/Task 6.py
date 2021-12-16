# Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или
# большим числом пробелов или символами конца строки.

n = int(input())
text = set()

for row in range(n):
    row = input().split()
    for word in range(len(row)):
        if row[word] not in text:
            text.add(row[word])
print(len(text))

# альтернативное решение
words = set()
for i in range(int(input())):
    words.update(input().split())
print(len(words))
