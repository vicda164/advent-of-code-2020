import unittest
from get_seat_id import get_seat_id


class TestClass(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_seat_id("FBFBBFFRLR"), 357)
        self.assertEqual(get_seat_id("BFFFBBFRRR"), 567)
        self.assertEqual(get_seat_id("FFFBBBFRRR"), 119)
        self.assertEqual(get_seat_id("BBFFBBFRLL"), 820)


if __name__ == "__main__":
    unittest.main()
