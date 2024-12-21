""" Домашнее задание по теме "Методы Юнит-тестирования" """

from runner_and_tournament import Runner
from runner_and_tournament import Tournament
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        runner_1 = Runner("Усэйн", 10)
        runner_2 = Runner("Андрей", 9)
        runner_3 = Runner("Ник", 3)
        return runner_1, runner_2, runner_3

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        distance_90 = Tournament(90, *[*self.setUp()[0:1], *self.setUp()[2:3]])
        self.all_results.update(distance_90.start())
        self.assertTrue(self.all_results[2], "Ник")
        self.tearDownClass()

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        distance_90 = Tournament(90, *self.setUp()[1:3])
        self.all_results.update(distance_90.start())
        self.assertTrue(self.all_results[2], "Ник")
        self.tearDownClass()

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        distance_90 = Tournament(90, *self.setUp()[0:3])
        self.all_results.update(distance_90.start())
        self.assertTrue(self.all_results[2], "Ник")
        self.tearDownClass()


if __name__ == "__main__":      # запуск теста
    unittest.main()
