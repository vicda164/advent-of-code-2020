
import unittest
from declaration import count_declarations
example_input = """abc

a
b
c

ab
ac

a
a
a
a

b
"""


class TestClass(unittest.TestCase):
    def test_1(self):
        groups = example_input.split("\n\n")
        self.assertEqual(count_declarations(groups), 11)

    def test_2(self):
        groups = example_input.split("\n\n")
        self.assertEqual(count_declarations(groups, True), 6)


if __name__ == "__main__":
    unittest.main()
