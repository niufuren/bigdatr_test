import unittest
import multiple_drone


class TestDroneMethods(unittest.TestCase):
    def setUp(self):
        self.multiple_drone = multiple_drone.MultipleDrone()

    def test_read_commands(self):
        '''the test_input.txt contains a string "xvx>^<"
        '''
        self.multiple_drone.read_commands("test/test_input.txt", 2, 1)
        self.assertEqual(self.multiple_drone.command,
                         ['x', 'x', '^'])

        self.multiple_drone.read_commands("test/test_input.txt", 2, 2)
        self.assertEqual(self.multiple_drone.command,
                         ['v', '>', '<'])

    def test_billboard_number_union(self):
        self.multiple_drone.snapshot.position = [(0,0),(1,1)]

        drone_second = multiple_drone.MultipleDrone()
        drone_second.snapshot.position =[(0,0)]

        self.assertEqual(self.multiple_drone.billboard_number_union(drone_second),
            2)

        drone_second.snapshot.position =[(1,0)]

        self.assertEqual(self.multiple_drone.billboard_number_union(drone_second),
            3)


if __name__ == '__main__':
    unittest.main()
