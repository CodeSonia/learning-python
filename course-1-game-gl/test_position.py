import unittest

from position import *


class TestPosition(unittest.TestCase):
    def test_position(self):
        self.assertEqual(position(1, 1), "1:1")

    def test_decode(self):
        self.assertEqual(decode("1:1"), [1, 1])

    def test_north(self):
        p = position(1, 1)
        self.assertEqual(north(p), "1:2")

    def test_south(self):
        p = position(1, 1)
        self.assertEqual(south(p), "1:0")

    def test_east(self):
        p = position(1, 1)
        self.assertEqual(east(p), "2:1")

    def test_west(self):
        p = position(1, 1)
        self.assertEqual(west(p), "0:1")

    def test_can_go_north(self):
        p = position(1, 1)
        self.assertEqual(can_go(p, ["1:2"]), ["North"])

    def test_can_go_north_south(self):
        p = position(1, 1)
        self.assertEqual(can_go(p, ["1:2", "1:0"]), ["North", "South"])

    def test_can_go_north_south_east(self):
        p = position(1, 1)
        self.assertEqual(can_go(p, ["1:2", "1:0", "2:1"]), [
                         "North", "South", "East"])

    def test_can_go_north_south_east_west(self):
        p = position(1, 1)
        self.assertEqual(can_go(p, ["1:2", "1:0", "2:1", "0:1"]), [
                         "North", "South", "East", "West"])
