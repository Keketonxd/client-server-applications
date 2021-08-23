"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = ['class', 'function', 'method']


def get_data(input_word):
    return type(input_word), input_word, len(input_word)


for word in words:
    print(get_data(word))
    word = bytes(word, encoding='utf-8')
    print(get_data(word))
