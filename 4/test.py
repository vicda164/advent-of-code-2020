import unittest
from passport import is_valid_passport, validate
TEST_INPUT = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


class MyTest(unittest.TestCase):

    def test_is_valid(self):
        passports = list(map(lambda passport: str(
            passport).replace("\n", " "), TEST_INPUT.split("\n\n")))
        print(passports)
        self.assertTrue(is_valid_passport(passports[0]))
        self.assertFalse(is_valid_passport(passports[1]))
        self.assertTrue(is_valid_passport(passports[2]))
        self.assertFalse(is_valid_passport(passports[3]))

    def test_nr_of_valid(self):
        passports = list(map(lambda passport: str(
            passport).replace("\n", " "), TEST_INPUT.split("\n\n")))
        print("nr_of_valids")
        self.assertEqual(validate(passports), 2)


if __name__ == "__main__":
    unittest.main()
