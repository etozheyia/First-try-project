# В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам.
# Для каждого файла известно, с какими действиями можно к нему обращаться:
#
# запись W,
# чтение R,
# запуск X.
#
# В первой строке содержится число N — количество файлов содержащихся в данной файловой системе. В следующих N строчках
# содержатся имена файлов и допустимых с ними операций, разделенные пробелами. Далее указано чиcло M — количество
# запросов к файлам. В последних M строках указан запрос вида Операция Файл. К одному и тому же файлу может быть
# применено любое колличество запросов.
#
# Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого запроса должна будет
# возвращать OK если над файлом выполняется допустимая операция, или же Access denied, если операция недопустима).

com = {}
for i in range(int(input())):
    row = input().split()
    if len(row) == 2:
        com[row[1]] = com.get(row[1], row[1]) + ' ' + row[0]
    elif len(row) == 3:
        com[row[1]] = com.get(row[1], row[1]) + ' ' + row[0]
        com[row[2]] = com.get(row[2], row[2]) + ' ' + row[0]
    else:
        com[row[1]] = com.get(row[1], row[1]) + ' ' + row[0]
        com[row[2]] = com.get(row[2], row[2]) + ' ' + row[0]
        com[row[3]] = com.get(row[3], row[3]) + ' ' + row[0]

read, execute, write = [], [], []
for i in com.values():
    if i[0] == 'R':
        read = ['read']
        read += i[2:].split()
    elif i[0] == 'X':
        execute = ['execute']
        execute += i[2:].split()
    else:
        write = ['write']
        write += i[2:].split()

for i in range(int(input())):
    row = input().split()
    if row[0] in read:
        if row[1] in read:
            print('OK')
        else:
            print('Access denied')
    elif row[0] in execute:
        if row[1] in execute:
            print('OK')
        else:
            print('Access denied')
    elif row[0] in write:
        if row[1] in write:
            print('OK')
        else:
            print('Access denied')
    else:
        print('Access denied')


# альтернативное решение 1
ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')

# альтернатвное решение 2
D = {}
for i in range(int(input())):
    a = input().split()
    D[a[0]] = a[1:]
for i in range(int(input())):
    r, t = input().split()
    if r == 'read':
        r = 'R'
    elif r == 'write':
        r = 'W'
    else:
        r = 'X'
    if r in D[t]:
        print("OK")
    else:
        print('Access denied')
