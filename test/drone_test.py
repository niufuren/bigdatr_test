import unittest
import drone


class TestDroneMethods(unittest.TestCase):
    def setUp(self):
        self.drone = drone.Drone()

    def test_read_commands(self):
        self.drone.read_commands("test/test_input.txt")
        self.assertEqual(self.drone.command,
                         ['x', 'v', 'x', '>', '^', '<'])

    def test_single_command_down(self):
        self.drone.command = 'v'
        self.drone.process()
        self.assertEqual(self.drone.movement.x, 0)
        self.assertEqual(self.drone.movement.y, -1)

    def test_single_command_up(self):
        self.drone.command = '^'
        self.drone.process()
        self.assertEqual(self.drone.movement.x, 0)
        self.assertEqual(self.drone.movement.y, 1)

    def test_single_command_left(self):
        self.drone.command = '<'
        self.drone.process()
        self.assertEqual(self.drone.movement.x, -1)
        self.assertEqual(self.drone.movement.y, 0)

    def test_single_command_right(self):
        self.drone.command = '>'
        self.drone.process()
        self.assertEqual(self.drone.movement.x, 1)
        self.assertEqual(self.drone.movement.y, 0)

    def test_single_command_snapshot(self):
        self.drone.command = 'x'
        self.drone.process()
        self.assertEqual(self.drone.snapshot.position, [(0, 0)])
        self.assertEqual(self.drone.snapshot.snapshot_num, [1])


if __name__ == '__main__':
    unittest.main()
