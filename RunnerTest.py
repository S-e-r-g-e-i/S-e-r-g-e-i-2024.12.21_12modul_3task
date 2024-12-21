""" Домашнее задание по теме "Простые Юнит-Тесты" """

from Runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        object_walk = Runner('name1')
        for i in range(10):
            object_walk.walk()
        self.assertEqual(object_walk.distance, 50)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        object_run = Runner('name2')
        for i in range(10):
            object_run.run()
        self.assertEqual(object_run.distance, 100)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        object_walk2 = Runner('name3')
        object_run2 = Runner('name4')
        for i in range(10):
            object_walk2.walk()
            object_run2.run()
        self.assertNotEqual(object_walk2.distance, object_run2.distance)


if __name__ == "__main__":      # запуск теста
    unittest.main()



