import random
import time
# !!! pip install Faker !!! write in project venv terminal
from Menu import dead_ship, ship_attack, ship_initialization

def menu():

    role_1 = int(input('Выберите роль первого игрока:\n'
                    '\t1. Человек\n'
                    '\t2. Искусственный интелект\n'
                    'Роль первого игрока: '))
    role_2 = int(input('\nВыберите роль второго игрока:\n'
                       '\t1. Человек\n'
                       '\t2. Искусственный интелект\n'
                       'Роль второго игрока: '))


    print('Бросаем монетку. Орёл или решка?\n')
    coin_flip = 0

    if role_1 == 1:
        print('Первый игрок - человек, выберите сторону:\n')
        coin_flip = int(input('\t1. Орёл\n'
              '\t2. Решка\n'
              'Ваш выбор: '))

    if role_1 == 2:
        print('Первый игрок - искусственный интелект, поэтому он сам выбирает...')
        time.sleep(3)
        coin_flip = random.randint(1,2)

    if coin_flip == 1:
        print('Первый игрок выбрал Орёл, второй - Решка.')

    if coin_flip == 2:
        print('Первый игрок выбрал Решка, второй - Орёл.')

    print()

    print('Бросаем монетку...')
    time.sleep(3)
    buff_flip = random.randint(1, 2)
    print('Выпало: ', 'Орёл' if  buff_flip == 1 else 'Решка.')

    print('Начинает первый игрок' if buff_flip == coin_flip else 'Начинает второй игрок.')

dict_ship = {
    1: ['A1', 'E1', 'A6', 'F10'],
    2: ['F6_G6', 'B8_C8', 'I7_I8'],
    3: ['G2_G4', 'D4_D6'],
    4: ['A10_D10']
}


enemy_greed = [[1 for _ in range(10)] for _ in range(10)]

# заполняем поле кораблями (словарь координат, поле)
def ship_initialization(dict_ship: dict, enemy_greed: list)-> list:
    list_ship = [i for i in dict_ship.values()]
    for coordinates in list_ship:
        if '_' in coordinates[0]:
            for coord in coordinates:
                buf = coord.split('_')

                #если буквы одинаковые - в столбик
                if buf[0][0] == buf[1][0]:

                    for rows in range(int(buf[0][1]) - 1, int(buf[1][1:])):
                        enemy_greed[rows][ord(buf[0][0].lower()) - 97] = 0
                # если буквы не одинаковые - в строку
                if buf[0][0] != buf[1][0]:
                    for columns in range(ord(buf[0][0].lower()) - 97, ord(buf[1][0].lower()) - 96):
                        enemy_greed[int(buf[0][1:]) - 1][columns] = 0
        else:
            for coord in coordinates:
                enemy_greed[int(coord[1:]) - 1][ord(coord[0].lower())- 97] = 0
    return enemy_greed

# атака корабля (позиция, поле)
def ship_attack(position: str, enemy_greed: list, empty_greed: list )-> list:
    if enemy_greed[int(position[1:]) - 1][ord(position[0].lower()) - 97] == 0:
        enemy_greed[int(position[1:]) - 1][ord(position[0].lower()) - 97] = 'X'
        empty_greed[int(position[1:]) - 1][ord(position[0].lower()) - 97] = enemy_greed[int(position[1:]) - 1][ord(position[0].lower()) - 97]
    else:
        enemy_greed[int(position[1:]) - 1][ord(position[0].lower()) - 97] = '*'


    return [enemy_greed, empty_greed]

# проверка корабля на смерть
def dead_ship(dict_ship: dict, enemy_greed: list):
    total_dead = 0
    list_ship = [i for i in dict_ship.values()]
    for coordinates in list_ship:
        if '_' in coordinates[0]:
            for coord in coordinates:
                buf = coord.split('_')
                counter = 0
                # если буквы одинаковые - в столбик
                if buf[0][0] == buf[1][0]:
                    #считает ранения
                    win_len = int(buf[1][1:]) - int(buf[0][1]) + 1

                    for rows in range(int(buf[0][1]) - 1, int(buf[1][1:])):
                        if enemy_greed[rows][ord(buf[0][0].lower()) - 97] == 'X':
                            counter += 1
                    if win_len == counter:
                        total_dead += 1
                # если буквы не одинаковые - в строку
                if buf[0][0] != buf[1][0]:
                    win_len = (ord(buf[1][0].lower())-97)-(
                                ord(buf[0][0].lower())-97)+1
                    for columns in range(ord(buf[0][0].lower())-97,
                                         ord(buf[1][0].lower())-97+1):
                        if enemy_greed[int(buf[0][1:])-1][columns] == 'X':
                            counter += 1
                    if win_len == counter:
                        total_dead += 1
                else:
                    for coord in coordinates:
                        if enemy_greed[int(coord[1:])-1][
                            ord(coord[0].lower())-97] == 'X':
                            total_dead += 1
                return total_dead