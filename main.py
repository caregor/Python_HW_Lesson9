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
Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

4.* (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
 Например:
 >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
 {  "А": { "П": ["Петр Алексеев"] },
    "И": { "И": ["Илья Иванов"] },
    "С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] }
 }
"""


# Task 1
# def to_dict(lst):
#     result = {}
#     for item in lst:
#         result[item] = item
#     return result
#
#
# source = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(to_dict(source))

# Task 2
# def biggest_dict(**kwargs):
#     my_dic.update(kwargs)
#
#
# my_dic = {'fist_one': "we can do it"}
# biggest_dict(second='we did it', third='we did it again')
#
# print(my_dic)

# Task 3
# def count_it(sequence):
#     seq_list = list(sequence)
#     result = {}
#     answer_dic = {}
#     for item in seq_list:
#         cnt = seq_list.count(item)
#         result[int(item)] = cnt
#
#     for _ in range(3):
#         max_val = max(result.values())
#         final_dict = {k: v for k, v in result.items() if v == max_val}
#         answer_dic.update(final_dict)
#         tmp = final_dict.keys()
#         tnp_int = list(tmp)
#         result.pop(tnp_int[0])
#     return answer_dic
#
#
# raw = '0000111223456789'
# print(count_it(raw))

# Task 4

def thesaurus_adv(*args):
    dict_by_name = {}
    dict_by_last_name = {}
    save_list = []
    i = 0
    for item in args:
        i += 1
        tmp_list = item.split()
        key_by_last_name = tmp_list[1][0][0]
        key_by_name = tmp_list[0][0][0]
        if key_by_last_name not in dict_by_last_name.keys():
            dict_by_name[key_by_name] = item
            dict_by_last_name[key_by_last_name] = dict_by_name
            dict_by_name = {}
        else:
            if key_by_name in dict_by_name.keys() or key_by_name == previous_key_by_name:
                save_list.append(item)
                save_list.append(previous_item)
                dict_by_name[key_by_name] = save_list
                dict_by_last_name[key_by_last_name] = dict_by_name
                dict_by_name = {}
            else:
                tmp_dict = dict_by_last_name[key_by_last_name]
                tmp_dict[key_by_name] = item
                dict_by_last_name[key_by_last_name] = tmp_dict
        previous_key_by_name = key_by_name
        previous_item = item

        save_list = []
    print(dict_by_last_name)

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
