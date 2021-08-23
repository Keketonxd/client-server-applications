"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

words = ['attribute', 'класс', 'функция', 'type']


def get_data(input_word):
    return type(input_word), input_word, len(input_word)


for word in words:
    print(get_data(word))
    word = bytes(word, encoding='utf-8')
    print(get_data(word))

print('ez')
