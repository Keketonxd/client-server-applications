"""
Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

yaml_test = {'cities': ['Moscow', 'Dublin', 'R\u012bga'],
             'age': 22,
             'dict': {'mama': f'{2300}\u00a5',
                      'papa': f'{12452}\u00a5',
                      'deda': f'{9190}\u00a5'}}

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(yaml_test, f, default_flow_style=True, allow_unicode=True)

# Не уверен, нужно ли было вернуть тоже в формате с кодовыми точками.
with open('file.yaml', 'r', encoding='utf-8') as f:
    print(yaml.load(f))
