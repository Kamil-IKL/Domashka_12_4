import rt_with_exceptions
import unittest


# Класс TournamentTest для тестирования турнира
class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        # словарь для хранения результатов тестов
        cls.all_results = {}

    def setUp(self):
        # создаю бегунов
        self.runner_first = rt_with_exceptions.Runner('Вася', 10)
        self.runner_second = rt_with_exceptions.Runner('Илья', 5)
        self.runner_third = rt_with_exceptions.Runner('Арсен', 10)

    @classmethod
    def tearDownClass(cls):
        print('\nВсе результаты:')
        for name, result in cls.all_results.items():  # метод ".items()" для вывода пары "ключ-значение" словаря в столбец
            print(f'\n{name}: ')
            for pacte, runner in result.items():  # раскрываю словарь result
                print(f'{pacte} место: {runner}')
        """
        Это мне для изучения, как вместо строк 22-25 можно написать в одну строку 
        (пересмотреть Модуль 9. Списковые сборки)
        """
        # _ = [print('забег:', x, ' - ', k, 'место:', z) for x, y in cls.all_results.items() for k, z in y.items()]

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    # Первый забег на 101м.:  runner_first и runner_second
    def test_usain_nik(self):
        tournament_101 = rt_with_exceptions.Tournament(101, self.runner_first, self.runner_second)
        results = tournament_101.start()
        self.all_results[f'{self.runner_first} и {self.runner_second}'] = results
        self.assertTrue(results[2] == 'Илья')

    def test_walk(self):
        obj_1 = runner.Runner("VALERA")
        for i in range(10):
            obj_1.walk()
            # print(obj_1.distance) # для проверки результата
        self.assertEqual(obj_1.distance, 50)



    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    # # Первый забег на 90м.: Усейн и Ник
    # def test_usain_nik(self):
    #     tournament_90 = rt_with_exceptions.Tournament(90, self.runner_usain, self.runner_nik)
    #     results = tournament_90.start()
    #     self.all_results['Усейн и Ник'] = results
    #     self.assertTrue(results[2] == 'Ник')

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    # # Второй забег на 90м.: Андрей и Ник
    # def test_andrey_nik(self):
    #     tournament_90 = rt_with_exceptions.Tournament(90, self.runner_andrey, self.runner_nik)
    #     results = tournament_90.start()
    #     self.all_results['Андрей и Ник'] = results
    #     self.assertTrue(results[2] == 'Ник')
    #
    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    # # Третий забег на 90м.: Усейн, Андрей и Ник
    # def test_usain_andrey_nik(self):
    #     tournament_90 = rt_with_exceptions.Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
    #     results = tournament_90.start()
    #     self.all_results['Усейн, Андрей и Ник'] = results
    #     self.assertTrue(results[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
