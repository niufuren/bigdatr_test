import unittest
import multiple_drone
import mock

TOTAL_DRONE_NUMBER = 2


class TestDroneMethods(unittest.TestCase):
    def setUp(self):
        self.multiple_drone_first = multiple_drone.MultipleDrone(
            TOTAL_DRONE_NUMBER,
            1
        )
        self.multiple_drone_second = multiple_drone.MultipleDrone(
            TOTAL_DRONE_NUMBER,
            2
        )

    def test_read_commands(self):
        '''the test_input.txt contains a string "xvx>^<"
        '''
        with mock.patch(
            'multiple_drone.MultipleDrone.process'
        ) as mock_process:
            self.multiple_drone_first.read_process_commands(
                "test/test_input.txt")
            self.multiple_drone_second.read_process_commands(
                "test/test_input.txt")

            process_parameter_list = [('x'), ('x'), ('^'), ('v'), ('>'), ('<')]
            mock_process.call_args_list == process_parameter_list

    def test_billboard_number_union(self):
        self.multiple_drone_first.snapshot.position = [(0, 0), (1, 1)]

        self.multiple_drone_second.snapshot.position = [(0, 0)]

        self.assertEqual(
            self.multiple_drone_first.billboard_number_union(
                self.multiple_drone_second),
            2)

        self.multiple_drone_second.snapshot.position = [(1, 0)]

        self.assertEqual(
            self.multiple_drone_first.billboard_number_union(
                self.multiple_drone_second),
            3)


if __name__ == '__main__':
    unittest.main()
