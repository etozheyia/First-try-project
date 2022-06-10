# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран
# всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.

filename = 'task_3.txt'
students = []
overall_score = 0
with open(filename) as file_list:
    for row in file_list:
        students.append(row.split(','))

student_mark_position = 1
passing_score = 3
weak_student = 0
for line in range(len(students)):
    for student_info in range(len(students[line])):
        if student_info == student_mark_position:
            overall_score += int(students[line][student_info])
            if int(students[line][student_info]) < passing_score:
                print(students[line][weak_student])

print(overall_score / len(students))
