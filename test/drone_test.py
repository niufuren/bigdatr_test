import unittest
import drone
import mock


class TestDroneMethods(unittest.TestCase):
    def setUp(self):
        self.drone = drone.Drone()

    def test_read_process_commands(self):
        with mock.patch('drone.Drone.process') as mock_process:
            self.drone.read_process_commands("test/test_input.txt")
            process_parameter_list = [('x'), ('v'), ('x'), ('>'), ('^'), ('<')]
            mock_process.call_args_list == process_parameter_list

    def test_single_command_down(self):
        self.drone.process('v')
        self.assertEqual(self.drone.movement.x, 0)
        self.assertEqual(self.drone.movement.y, -1)

    def test_single_command_up(self):
        self.drone.process('^')
        self.assertEqual(self.drone.movement.x, 0)
        self.assertEqual(self.drone.movement.y, 1)

    def test_single_command_left(self):
        self.drone.process('<')
        self.assertEqual(self.drone.movement.x, -1)
        self.assertEqual(self.drone.movement.y, 0)

    def test_single_command_right(self):
        self.drone.process('>')
        self.assertEqual(self.drone.movement.x, 1)
        self.assertEqual(self.drone.movement.y, 0)

    def test_single_command_snapshot(self):
        self.drone.process('x')
        self.assertEqual(self.drone.snapshot.position, [(0, 0)])
        self.assertEqual(self.drone.snapshot.snapshot_num, [1])


if __name__ == '__main__':
    unittest.main()
