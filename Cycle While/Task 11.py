# Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы.
# Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию.
# После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:
#
# Команда	Описание
# push n - Добавить в стек число n (значение n задается после команды). Программа должна вывести ok. - (с параметром)
# pop -	Удалить из стека последний элемент. Программа должна вывести его значение. - (без параметра)
# back - Программа должна вывести значение последнего элемента, не удаляя его из стека. - (без параметра)
# size - Программа должна вывести количество элементов в стеке. - (без параметра)
# clear - Программа должна очистить стек и вывести ok. - (без параметра)
# show - Программа должна вывести стек. - (без параметра)
# exit - Программа должна вывести bye и завершить работу. - (без параметра)
#
# Входные данные
# Команды управления стеком вводятся в описанном ранее формате по 1 на строке.
# Гарантируется, что набор входных команд удовлетворяет следующим требованиям: максимальное количество элементов в стеке
# в любой момент не превосходит 100, все команды pop и back корректны, то есть при их исполнении в стеке содержится
# хотя бы один элемент.
#
# Пример выполнения программы:
# входные данные                      выходные данные
# push 3                              ok
# push 14                             ok
# size                                2
# clear                               ok
# push 1                              ok
# back                                1
# push 2                              ok
# back                                2
# pop                                 2
# size                                1
# pop                                 1
# size                                0
# exit                                bye

def push(n):
    stack_list = stack.append(n)
    return stack_list


stack = []
command = input()

while command != 'exit':
    if command == 'push':
        push(int(input()))
        print('Ok')
        if len(stack) == 101:
            stack.pop()
            print(stack)
            print('Stack reached maximum size')
            print('The program is going to finish')
            break
    elif command == 'pop' and len(stack) >= 1:
        print(stack[-1])
        stack.pop()
    elif command == 'back' and len(stack) >= 1:
        print(stack[-1])
    elif command == 'size':
        print(len(stack))
    elif command == 'clear':
        stack = []
        print('Ok')
    elif command == 'show' and len(stack) >= 1:
        print(stack)
    elif command != 'push' or 'pop' or 'back' or 'size' or 'clear' or 'show':
        print('Incorrect command')
    elif command == 'pop' or 'back' or 'show' and len(stack) < 1:
        print('Stack was not found')
    else:
        print('Bye')
    command = input()
