# В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor).
# Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является предком B,
# при этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.
#
# Формат входных данных аналогичен предыдущей задаче.
# Для каждого запроса выведите наименьшего общего предка данных элементов.

def ancestors(child, p_tree):
    result = []
    result.append(child)
    while child in p_tree:
        child = p_tree[child]
        result.append(child)
    return result


p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

m = int(input())
for i in range(m):
    child_1, child_2 = input().split()
    ancestors_for_1 = set(ancestors(child_1, p_tree))
    for ancestor in ancestors(child_2, p_tree):
        if ancestor in ancestors_for_1:
            print(ancestor)
            break
