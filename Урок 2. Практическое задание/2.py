"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json
from sys import argv


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f:
        orders_list = json.load(f)
    order = {}
    order['item'] = item
    order['quantity'] = quantity
    try:
        order['price'] = float(price)
    except ValueError:
        order['price'] = None
    order['buyer'] = buyer
    order['date'] = date
    orders_list['orders'].append(order)
    with open('orders.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(orders_list, indent=4, ensure_ascii=False))


write_order_to_json('папа', 'aqsd', '12', 'asd', 'qw')
