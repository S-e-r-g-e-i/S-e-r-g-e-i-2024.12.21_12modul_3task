""" Домашнее задание по теме "Систематизация и пропуск тестов" """

import unittest
import RunnerTest
import TournamentTest

Run_Tour_TS = unittest.TestSuite()
Run_Tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
Run_Tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

Runner_Tournament = unittest.TextTestRunner(verbosity=2)
Runner_Tournament.run(Run_Tour_TS)