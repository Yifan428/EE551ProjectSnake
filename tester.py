import unittest
from gamesnake import *


class MyTest(unittest.TestCase):
    def setUp(self):
        head.direction = "stop"

    def test_up(self):
        go_up()
        self.assertEqual(head.direction, 'up')

    def test_down(self):
        go_down()
        self.assertEqual(head.direction, 'down')

    def test_left(self):
        go_left()
        self.assertEqual(head.direction, 'left')

    def test_right(self):
        go_right()
        self.assertEqual(head.direction, 'right')

    def test_up_down(self):
        go_up()
        self.assertEqual(head.direction, 'up')
        go_down()
        self.assertEqual(head.direction, 'up')

    def test_down_up(self):
        go_down()
        self.assertEqual(head.direction, 'down')
        go_up()
        self.assertEqual(head.direction, 'down')

    def test_letf_right(self):
        go_left()
        self.assertEqual(head.direction, 'left')
        go_right()
        self.assertEqual(head.direction, 'left')

    def test_right_left(self):
        go_right()
        self.assertEqual(head.direction, 'right')
        go_left()
        self.assertEqual(head.direction, 'right')


if __name__ == '__main__':
    unittest.main()
