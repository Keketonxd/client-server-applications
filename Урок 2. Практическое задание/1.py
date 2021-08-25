import chardet
import csv
# import re


files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
topics = ['Название ОС',  'Код продукта',
          'Изготовитель системы', 'Тип системы']
for_csv = []

# Что-то странное было с кодировкой, а при перезаписи получались пустые строки между данными


def recoder():
    for file in files:
        with open(file, 'rb') as f:
            text = f.read()
            encoding = chardet.detect(text)
            text = text.decode(encoding['encoding'])

        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)

        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open(file, 'w', encoding='utf-8') as f:
            [f.write(line) for line in lines if line.strip()]


def get_data(list_of_files):
    for file in list_of_files:
        with open(file, 'r', encoding='utf-8') as f:
            charachteristics = []
            for line in f.readlines():
                for topic in topics:
                    if line.split(':')[0] == topic:
                        charachteristics.append(line.split(':')[1].strip())
            if charachteristics:
                for_csv.append(charachteristics)


# Почему-то не находит все совпадения.
    # with open(file, 'r', encoding='utf-8') as f:
    #     for topic in topics:
    #         for line in f.readlines():
    #             if re.search(topic, line):
    #                 print('Найдено!')
def write_to_csv(folder):
    for_csv.append(topics)
    get_data(files)
    with open(folder, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in for_csv:
            f_n_writer.writerow(row)


# Непонятно, почему так работает с порядком столбцов(подправил просто, но вне зависимости от последовательности в files, выдаёт только в такой последовательности данные)
write_to_csv('1.csv')
