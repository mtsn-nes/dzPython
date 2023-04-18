"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def calculate(*args):
    average = sum(args) / len(args)
    above_average = [num for num in args if num > average]
    return (average, above_average)
print(calculate(2,8,6,1))