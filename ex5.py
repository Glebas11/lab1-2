def task():
    spares = {
        'подшипник': ['подшипник', 60, 10],
        'ремень ГРЭМ': ['ремень ГРЭМ', 125, 15],
        'прокладка': ['прокладка', 200, 1]
    }
    characteristics = ['', ' гарантия(тыс км)', ' шт']
    menu = '''
1 - Описание запчастей 
2 - цена запчасти
3 - количество запчастей
4 - показать все характеристики
5 - купить
6 - выйти
    '''
    while True:
        try:
            a = int(input('Выберите операцию' + menu))
            if a == 1:
                    for i in spares:
                        print(i + ' ' + spares[i][0])
            elif a==2:
                    for i in spares:
                        print(i + ' ' + str(spares[i][1]) + ' руб')
            elif a == 3:
                    for i in spares:
                        print(i + ' ' + str(spares[i][2]) + ' шт')
            elif a == 4:
                    for i in spares:
                        print(i)
                        for _ in range(len(spares[i])):
                            print(str(spares[i][_]) + characteristics[_])
            elif a == 5:
                    spares_name = input('Введите название запчасти: ')
                    quantity = int(input('Введите количество: '))
                    if spares[spares_name][2] - quantity < 0:
                        raise ValueError
                    print('Произошла покупка:')
                    print(
                        f"Вы купили {quantity} запчастей {spares_name}, осталось {spares[spares_name][2] - quantity} шт")
            else:
                    break
        except KeyError:
            print('Неверный ввод запчасти')

        except ValueError:
            print('Слишком большое количество')


task()