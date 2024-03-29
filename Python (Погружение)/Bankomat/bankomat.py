import logging

logging.basicConfig(filename='bankomat.log', level=logging.INFO, encoding='UTF-8')
logger = logging.getLogger()


def get_reach_taks(balance:int)-> int:
    """
    Функкция вычисления налога на богатство
    """
    logger.info('Работа функции налог на богатство')

    if balance > 5_000_000: # Если на балансе больше 5 ти млн

        logger.info('Списание налога на богатство')

        balance *= 0.9      # Cписывается налог на богатство
    return balance



def add_money(balance:int) -> int:
    """
    Функция добавления средств на счет
    """
    logger.info('Работа функции пополнение счета')

    balance = get_reach_taks(balance) # Проверка на списание налога на богатство
    success = False

    logger.info('Ввод суммы пополнения')

    value = int(input('Введите сумму пополнения: '))  # Ввод суммы пополнения баланса

    logger.info('Проверка на кратность 50 ти')

    if value % 50 == 0:                 # Если сумма кранта 50 ти
        logger.info('Баланс пополнен успешно')
        balance += value                            # Пополняем баланс
        success = True        
    else:
        logger.info('Некорректная сумма ввода ')
        print('Введите сумму, кратную 50.')         # В проивном случае просим ввести сумму
    return balance, success                         # Кратную 50 ти




def calc_comiss(value: int) -> int:
    """
    Функция коммиссии за снятие средств
    """
    logger.info('Работа функции коммиссия за снятие средств ')
    logger.info('Расчет коммисии')
    result = value * 0.015  # Рассчитываем сумму процента
    if result < 30:         # Если сумма комиссии  меньше 30 ти уе
        logger.info('Коммиссия меньше 30 уе, списание 30 уе')
        result = 30          # Списываем 30 уе
    if result > 600:         # Если сумма коммиссии больше 600 уе
        logger.info('Коммиссия больше  600 уе, списание 600 уе')
        result = 600         # Списываем 600 уе
    return result

def get_money(balance:int) -> int:
    """
    Функция  снятия средств
    """
    logger.info('Работа функции снятие средств')
    balance = get_reach_taks(balance)      # Проверка наличия налога на богатство
    success = False
    logger.info('Ввод суммы снятия')
    value = int(input('Введите сумму для снятия: '))  # Ввод суммы снятия средств
    logger.info('Проверка кратности 50 ти')
    if value % 50 == 0:                             # Проверка на кратность 50 ти
        comiss = calc_comiss(value)                  # Рассчет комиссии за снятие 
        if balance >= (comiss + value):
            logger.info('Расчет суммы снятия средств c учетом комисии') 
            balance = balance - value - comiss      # Вычитаем из баланса сумму снятия и комисии
            logger.info('Успешнное снятие средств')
            success = True
        else:
            logger.info('Недостаточный баланс')
            print('У вас недостаточный баланс.')      # Если сумма на счете недостаточная
    else:
        logger.info('Введена некорректная сумма')
        print('У вас некорректная сумма денег.')      # Если введена некорректная сумма для снятия средств
    return balance, success



count = 0     # Счетчик операций
balance = 0    # Началный баланс
while True:
    print(' 1 - пополнить баланс 2\n 2 - Снять деньги \n 3 - Выход')   # Возможные опреции
    sel = int(input('Сделайте ваш выбор: '))
    if sel == 1:                               # Выбор операции пополнить баланс
        logger.info('Выбрана опреция пополнить баланс')
        logger.info('Пополнение беленса')
        balance, success = add_money(balance)   # Функция пополнения баланса

    elif sel == 2:                              # Выбор операции снятие средств
        logger.info('Выбрана опреция снятие средств')
        logger.info('Снятие средств со счета')
        balance, success = get_money(balance)   # Функция снятия средств

    elif sel == 3:                              # Выбор функции выход
        logger.info('Выбрана опреция выход')
        logger.info('Заврешение работы')
        break                                    # Заврешение работы банкомата

    else:
        logger.info('Выбрана некорректная опреряция')
        print('Введите корректный выбор команды.')   # Некорректный выбор опрерации

    if success:
        count += 1
        logger.info('Вывод баланса')  # Вывод баланса
        print(f'Ваш баланс составляет: {balance}')

    if count == 3:                                   # Начисление процента за каждую 3 -ю
        logger.info('Начисление процента за каждую 3ю опрецию снятия/ внесения на счет')
        balance *= 1.03                              # операцию снятия или пополнения
        count = 0