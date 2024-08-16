import logging
import unittest
from Domashka_12_4 import rt_with_exceptions

"""
Обрати внимание, что при использовании уровня логирования `INFO`, все сообщения с уровнями `DEBUG` 
будут игнорироваться, и в лог файл будут записаны только сообщения с уровнями `INFO`, `WARNING`, `ERROR` и `CRITICAL`
"""

logging.basicConfig(
    level=logging.INFO,  # уровень логирования
    filemode='w',  # Название файла # Режим - 'w' для перезаписи, "а" - для добавления
    filename='runner_tests.log',  # Название файла
    encoding='utf-8',  # Кодировка
    format='%(asctime)s | %(levelname)s | %(message)s')  # Формат вывода


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            name_r1 = 'ВАСЯ'
            r1 = rt_with_exceptions.Runner(name_r1, -10)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning(f'"test_walk", неверная скорость для Runner(бегуна): {name_r1}', exc_info=True)

    def test_run(self):
        try:
            name_r2 = 123456
            r2 = rt_with_exceptions.Runner(name_r2, 5)
            for i in range(10):
                r2.run()
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning(f'"test_run", неверный тип данных для объекта Runner(бегуна): {name_r2}', exc_info=True)

    def test_challenge(self):
        try:
            r1 = rt_with_exceptions.Runner('Валера', 25)
            r2 = rt_with_exceptions.Runner('Явдат', 320)
            for i in range(10):
                r1.walk()
                r2.run()
            self.assertNotEqual(r1.distance, r2.distance)
            logging.info('"test_challenge" успешно пройден')
        except:
            logging.warning(f'"test_challenge", неверно указан аргумент для Runner(бегуна)', exc_info=True)


"""
ОБРАТИ ВНИМАНИЕ !
Если логирование запустишь после теста(ов), то работать не будет !!!! 
ОБЯЗАТЕЛЬНО ЛОГИРОВАНИЕ ДОЛЖНО БЫТЬ ПЕРЕД ТЕСТАМИ (ВВЕРХУ)

# if __name__ == '__main__':
#     logging.basicConfig(
#     level=logging.INFO,  # уровень логирования
#     filemode='w',  # Название файла # Режим - 'w' для перезаписи
#     filename='runner_tests.log',  # Название файла
#     encoding='utf-8',  # Кодировка
#     format='%(asctime)s | %(levelname)s | %(message)s')  # Формат вывода

"""
