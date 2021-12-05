import time
import random


def menu():
    import datetime

  #  a = datetime.datetime.now().ctime().replace(' ', '').replace(':', '') + '.txt'

  #  with open(a, 'w', encoding='utf-8') as file:

    name_player1 = input('\nПервый игрок, введите свое имя: ')


    print(f'Имя первого игрока - {name_player1}')


    name_player2 = input('\nВторой игрок, ввудите свое имя: ')

    print(f'Имя первого игрока - {name_player2}')

    # Расставляем корабли#

    print(f'\n{name_player1}, выберите сторону: ')
    coin_flip = int(input('\t1. Орёл\n'
                          '\t2. Решка\n'
                          'Ваш выбор: '))


    if coin_flip == 1:
        print(f'Игрок {name_player1} выбрал Орёл, игроку {name_player2} достается - Решка.')

    else:
        print(f'Игрок {name_player1} выбрал Решка, игроку {name_player2} достается - Орёл.')

    print('Cудьба бросает монетку. Орёл или решка?\n')

    print('\nБросаем монетку...')
    time.sleep(3)
    buff_flip = random.randint(1, 2)

    print('Выпало: ', 'Орёл' if buff_flip == 1 else 'Решка.')
    print('Начинает первый игрок\n' if buff_flip == coin_flip else 'Начинает второй игрок.\n', '_' * 60)

    win = True
    counter1 = 0

    counter2 = 0
    enemy_greed1 = [[1 for _ in range(10)] for _ in range(10)]

    enemy_greed2 = [[1 for _ in range(10)] for _ in range(10)]

    dict_ship1 = {
        1: ['A1', 'E1', 'A6', 'F10'],
        2: ['F6_G6', 'B8_C8', 'I7_I8'],
        3: ['G2_G4', 'D4_D6'],
        4: ['A10_D10']
    }

    dict_ship2 = {
        1: ['A1', 'E1', 'A6', 'F10'],
        2: ['F6_G6', 'B8_C8', 'I7_I8'],
        3: ['G2_G4', 'D4_D6'],
        4: ['A10_D10']
    }

    enemy_greed1 = ship_initialization(dict_ship1, enemy_greed1)
    enemy_greed11 = [[1 for _ in range(10)] for _ in range(10)]
    empty_greed1 = [[1 for _ in range(10)] for _ in range(10)]

    enemy_greed2 = ship_initialization(dict_ship2, enemy_greed2)
    enemy_greed22 = [[1 for _ in range(10)] for _ in range(10)]
    empty_greed2 = [[1 for _ in range(10)] for _ in range(10)]
    key_access = 0
    if buff_flip == coin_flip:
        key_access = 1
    else: key_access = 2

    while True:

        if key_access == 1:

            coord1 = input('\nПервый игрок, введите координату: ')
            a = ship_attack(coord1, enemy_greed2, empty_greed1)
            enemy_greed2, empty_greed1 = a[0], a[1]
            print('Таблица первого игрока:')
            for i in enemy_greed1:
                print(i)

            print('Таблица попаданий по противнику 2')
            for i in empty_greed1:
                print(i)

            counter1 = dead_ship(dict_ship2, enemy_greed2)
            print(f'всего убито {counter1}')

            if counter1 == 10:
                print('Выйграл первый')
                break

            key_access = 2

        if key_access == 2:

            coord2 = input('\nВторой игрок, введите координату: ')
            a = ship_attack(coord2, enemy_greed1, empty_greed2)
            enemy_greed1, empty_greed2 = a[0], a[1]
            print('Таблица второго игрока:')
            for i in enemy_greed2:
                print(i)

            print('Таблица попаданий по противнику 1\n')
            for i in empty_greed2:
                print(i)
            counter2 = dead_ship(dict_ship1, enemy_greed1)
            print(f'всего убито {counter2}')

            if counter2 == 10:
                print('Выйграл второй')
                break
            key_access = 1


menu()