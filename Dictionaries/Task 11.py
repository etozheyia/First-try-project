# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
#
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота
# равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
#
# Вам дано генеалогическое древо, определите высоту всех его элементов.
#
# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя
# для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
#
# Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого
# элемента необходимо вывести его высоту.
#
# Примечание
# Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n2) (не считая
# сложности обращения к элементам словаря).

def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])


p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

heights = {}
p_tree_keys, p_tree_values = set(p_tree.keys()), set(p_tree.values())
p_tree_common = p_tree_keys.union(p_tree_values)
for man in p_tree_common:
    heights[man] = height(man)

for key, value in sorted(heights.items()):
    print(key, value)
