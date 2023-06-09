from solution import zadanie_a
import unittest

class LongestStreakTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(zadanie_a("<<>"), 2)

    def test_2(self):
        self.assertEqual(zadanie_a("<><><><><><>"), 1)

    def test_3(self):
        self.assertEqual(zadanie_a("<>>><<"), 3)

    def test_4(self):
        self.assertEqual(zadanie_a("<<<<<<<<>>><<"), 8)

    def test_5(self):
        self.assertEqual(zadanie_a("<<>>><>>><<"), 3)

if __name__ == '__main__':
    unittest.main()