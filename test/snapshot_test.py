import unittest
import snapshot
import movement


class TestSnapshotMethods(unittest.TestCase):
    def setUp(self):
        self.snapshot = snapshot.Snapshot()
        self.movement = movement.Movement()
        self.movement.x = 1
        self.movement.y = 1

    def test_billboard_shot(self):
        self.snapshot.billboard_shot(self.movement)
        self.assertTrue(self.snapshot.position, (1, 1))
        self.assertEqual(self.snapshot.snapshot_num[0], 1)

        self.snapshot.billboard_shot(self.movement)
        self.assertEqual(self.snapshot.snapshot_num[0], 2)

    def test_unique_billboard_number(self):
        self.assertEqual(self.snapshot.unique_billboard_number(), 0)

        self.snapshot.billboard_shot(self.movement)
        self.assertEqual(self.snapshot.unique_billboard_number(), 1)


if __name__ == '__main__':
    unittest.main()
