# Напишите функцию для вычисления 5/0 и используйте try/except для отлова исключения DivisionError.

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Невозможно поделить на 0')


a, b = 5, 0
print(division(a, b))
