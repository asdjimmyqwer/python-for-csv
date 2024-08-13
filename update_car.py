import csv
import random


file_path = 'car_number.csv'


your_name = 'zxcv'
your_vehicle_number = 'ogh7542py'


with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)


def is_duplicate(vehicle_number, rows):
    for row in rows:
        if row[1] == vehicle_number:
            return True
    return False


def insert_randomly(name, vehicle_number, rows):
    if is_duplicate(vehicle_number, rows):
        print(f'車牌號碼 {vehicle_number} 已經存在於名單中。')
        return False, rows

    random_index = random.randint(1, len(rows))
    new_row = [name, vehicle_number]
    rows.insert(random_index, new_row)
    return True, rows


inserted, updated_rows = insert_randomly(your_name, your_vehicle_number, rows)


if inserted:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)
    print('已成功插入你的名字和車牌號碼，並檢查是否重複。')
