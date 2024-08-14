import logging
import rt_with_exceptions

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')


first = rt_with_exceptions.Runner('Вася', 10)
second = rt_with_exceptions.Runner('Илья', 5)

t = rt_with_exceptions.Tournament(101, first, second)
print(t.start())
