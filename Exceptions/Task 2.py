# Добавьте в тело этой функции оператор try-except, который обрабатывает возможную ошибку IndexError,
# которая может возникнуть, если указанный индекс превышает длину списка.
# Выведите сообщение об ошибке, если это произойдет:
# def print_list_element(thelist, index):
#     print(thelist[index])

def print_list_element(thelist, index):
    try:
        return thelist[index]
    except IndexError:
        print('Индекс превышает длину списка')


a = input().split()  # вводим список элементов
i = int(input())
print(print_list_element(a, i))
