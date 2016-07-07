import unittest
import movement


class TestMovementMethods(unittest.TestCase):
    def setUp(self):
        self.movement = movement.Movement()

    def test_move_up(self):
        self.movement.move_up()
        self.assertEqual(self.movement.y, 1)

    def test_move_down(self):
        self.movement.move_down()
        self.assertEqual(self.movement.y, -1)

    def test_move_right(self):
        self.movement.move_right()
        self.assertEqual(self.movement.x, 1)

    def test_move_left(self):
        self.movement.move_left()
        self.assertEqual(self.movement.x, -1)

if __name__ == '__main__':
    unittest.main()
