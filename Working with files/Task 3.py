# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран
# всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.

filename = 'task_3.txt'
students = []
overall_score = 0
with open(filename, encoding="utf8") as file_list:
    for row in file_list:
        students.append(row.split(','))

for i in range(len(students)):
    for j in range(len(students[i])):
        if j == 1:
            overall_score += int(students[i][j])
            if int(students[i][j]) < 3:
                print(students[i][0])

print(overall_score / len(students))
