# Учительница задала Пете домашнее задание — в заданном тексте расставить ударения в словах, после чего поручила Васе
# проверить это домашнее задание. Вася очень плохо знаком с данной темой, поэтому он нашел словарь, в котором указано,
# как ставятся ударения в словах. К сожалению, в этом словаре присутствуют не все слова. Вася решил, что в словах,
# которых нет в словаре, он будет считать, что Петя поставил ударения правильно, если в этом слове Петей поставлено
# ровно одно ударение.
#
# Оказалось, что в некоторых словах ударение может быть поставлено больше, чем одним способом. Вася решил, что в этом
# случае если то, как Петя поставил ударение, соответствует одному из приведенных в словаре вариантов, он будет
# засчитывать это как правильную расстановку ударения, а если не соответствует, то как ошибку.
#
# Вам дан словарь, которым пользовался Вася и домашнее задание, сданное Петей. Ваша задача — определить
# количество ошибок, которое в этом задании насчитает Вася.
#
# Вводится сначала число N — количество слов в словаре.
#
# Далее идет N строк со словами из словаря. Каждое слово состоит не более чем из 30 символов. Все слова состоят из
# маленьких и заглавных латинских букв. В каждом слове заглавная ровно одна буква — та, на которую попадает ударение.
# Слова в словаре расположены в алфавитном порядке. Если есть несколько возможностей расстановки ударения в одном
# и том же слове, то эти варианты в словаре идут в произвольном порядке.
#
# Далее идет упражнение, выполненное Петей. Упражнение представляет собой строку текста, суммарным объемом не более
# 300000 символов. Строка состоит из слов, которые разделяются между собой ровно одним пробелом. Длина каждого слова
# не превышает 30 символов. Все слова состоят из маленьких и заглавных латинских букв (заглавными обозначены те буквы,
# над которыми Петя поставил ударение). Петя мог по ошибке в каком-то слове поставить более одного ударения или не
# поставить ударения вовсе.
# Выведите количество ошибок в Петином тексте, которые найдет Вася.
#
# Примечания к примерам тестов
#
# 1. В слове cannot, согласно словарю возможно два варианта расстановки ударения. Эти варианты в словаре могут быть
# перечислены в любом порядке (т.е. как сначала cAnnot, а потом cannOt, так и наоборот). Две ошибки,
# совершенные Петей — это слова be (ударение вообще не поставлено) и fouNd (ударение поставлено неверно). Слово thE
# отсутствует в словаре, но поскольку в нем Петя поставил ровно одно ударение, признается верным.
#
# 2. Неверно расставлены ударения во всех словах, кроме The (оно отсутствует в словаре, в нем поставлено ровно
# одно ударение). В остальных словах либо ударные все буквы (в слове PAGE), либо не поставлено ни одного ударения.

accents = {}
for i in range(int(input())):
    word = input()
    base_form = word.lower()
    if base_form not in accents:
        accents[base_form] = set()
    accents[base_form].add(word)
mistakes = 0
home_work = input().split()

for word in home_work:
    base_form = word.lower()
    if (base_form in accents and word not in accents[base_form]
            or len([l for l in word if l.isupper()]) != 1):
        mistakes += 1

print(mistakes)
