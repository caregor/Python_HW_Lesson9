"""
1. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый
элемент списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам
задания ключей в словарях.

2. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), которая
принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

3. Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который в качестве
ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в
имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
Функция должна возвратить словарь из 3-х самых часто встречаемых чисел. 4.* (вместо задачи 3) Написать функцию
thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором
ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в
которых фамилия начинается с соответствующей буквы.
 Например:
 >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
 { "А": { "П": ["Петр Алексеев"] },
     "И": { "И": ["Илья Иванов"] },
 "С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] } }
"""


# Task 1
def to_dict(lst):
    result = {}
    for item in lst:
        result[item] = item
    return result


source = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(to_dict(source))
