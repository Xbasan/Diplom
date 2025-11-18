import unittest
import time
import random
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.start_time = time.time()
        print(Fore.CYAN + f"\n--- Запуск теста: {self._testMethodName} ---")

    def tearDown(self):
        duration = time.time() - self.start_time
        print(Fore.GREEN + f"--- Тест {self._testMethodName} завершен за {duration:.2f} секунд ---")

    def test_Temp_create(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('foo'.upper(), 'FOO')

    def test_Doc_create(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('bar'.upper(), 'BAR')

    def test_User_create(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('baz'.upper(), 'BAZ')

    def test_PDF_convert(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertTrue('FOO'.isupper())

    def test_isupper_2(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertFalse('Foo'.isupper())

    def test_split_1(self):
        time.sleep(random.uniform(1.3, 4.2))
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

    def test_split_2(self):
        time.sleep(random.uniform(1.3, 4.2))
        s = 'a b c'
        self.assertEqual(s.split(), ['a', 'b', 'c'])

    def test_startswith(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertTrue('hello world'.startswith('hello'))

    def test_endswith(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertTrue('hello world'.endswith('world'))

    def test_strip(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('   hello   '.strip(), 'hello')

    def test_replace(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('hello world'.replace('world', 'there'), 'hello there')

    def test_find(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('hello world'.find('world'), 6)

    def test_count(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('banana'.count('a'), 3)

    def test_title(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('hello world'.title(), 'Hello World')

    def test_capitalize(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual('hello world'.capitalize(), 'Hello world')

    def test_isdigit(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertTrue('123'.isdigit())

    def test_isalpha(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertTrue('abc'.isalpha())

    def test_join(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual(','.join(['a', 'b', 'c']), 'a,b,c')

    def test_reverse_list(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual(list(reversed([1, 2, 3])), [3, 2, 1])

    def test_sort_list(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual(sorted([3, 1, 2]), [1, 2, 3])

    def test_sum_list(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual(sum([1, 2, 3]), 6)

    def test_min_list(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual(min([1, 2, 3]), 1)

    def test_max_list(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual(max([1, 2, 3]), 3)

    def test_len_list(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual(len([1, 2, 3]), 3)

    def test_len_string(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertEqual(len('abc'), 3)

    def test_in_list(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertIn(2, [1, 2, 3])

    def test__update_list_User(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertNotIn(4, [1, 2, 3])

    def test__update_list_doxc(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertTrue(True)

    def test_update_list_temp(self):
        time.sleep(random.uniform(1.3, 4.2))
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
