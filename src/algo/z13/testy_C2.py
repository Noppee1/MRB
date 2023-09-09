import unittest
from random import randint
from solution_C2 import *



class TaskC2Tests(unittest.TestCase):

    def test_1(self):
        x1,y1,x2,y2 = randint(1,8),randint(1,8),randint(1,8),randint(1,8)
        move = min_knight_moves(x1,y1,x2,y2)
        print(x1,y1,x2,y2)
        self.assertEqual(move,)


if __name__ == '__main__':
    unittest.main()
