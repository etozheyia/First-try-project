# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.

a = [int(i) for i in input().split()]
count = 0
for i in range(len(a)):
    for t in range(len(a)):
        if i != t and a[i] == a[t]:
            count += 1
print(count // 2)