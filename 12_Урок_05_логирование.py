import math
import logging

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f'Делим {a} / {b}')
        return a / b
    except ZeroDivisionError as err:
        logging.error('Делить на ноль нельзя', exc_info=True)
        return 0


def sqrt(a):
    try:
        math.sqrt(a)
        logging.info(f'извлекаем квадратный корень из {a}')
        return math.sqrt(a)
    except ValueError as err:
        logging.error(f'Отрицательное число {a}', exc_info=True)
        return 0

def pow(a,b):
    return a**b


if __name__ == '__main__':
    """
    Пять основных уровней сообщений
    """
    # logging.debug('Самый низкий уровень: ежедневные сообщения о программе')
    # logging.info('Низкий уровень: информационные сообщения')
    # logging.warning('Средний уровень: внимание!!! что-то происходит не так (предупреждение о потенциальных ошибках)')
    # logging.error('Высокий уровень: Конкретная ошибка в программе')
    # logging.critical('Самый высокий уровень: все плохо, сообщение из-за чего программа не работает')

    """
    Пример записи логов в файл
    """
    logging.basicConfig(level=logging.INFO, filemode="w", filename='log_k_uroku_05.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    print(div(3,4))
    print(div(3, 0))
    print(sqrt(16))
    print(sqrt(-16))

