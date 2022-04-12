# Эта функция добавляет элемент в список внутри словаря списков. Перепишите ее, чтобы использовать оператор try-except,
# который обрабатывает возможную ошибку KeyError, если список с указанным именем еще не существует в словаре,
# вместо того, чтобы заранее проверять, существует ли он. Включите в блок try-except, блоки else и finally:
# def add_to_list_in_dict(thedict, listname, element):
#     if listname in thedict:
#         l = thedict[listname]
#         print("%s уже имеет %d элементов." % (listname, len(l)))
#     else:
#         thedict[listname] = []
#         print("Создано %s." % listname)
#
#     thedict[listname].append(element)
#
#     print("Добавил %s к %s." % (element, listname))

def add_to_list_in_dict(thedict, listname, element):
    explanatory_msg = ''
    try:
        thedict[listname].append(element)
    except KeyError:
        thedict[listname] = []
        thedict[listname].append(element)
        explanatory_msg = f'{listname} не существует. \nСоздано {listname}'
    else:
        explanatory_msg = f'{listname} был обнаружен в словаре.'
    finally:
        return explanatory_msg + f'\nДобавил {element} к {listname}'
