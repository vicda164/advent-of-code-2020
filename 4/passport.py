

def is_valid_passport(passport):
    """
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)          Mandatory
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)      OK, if only this one is missing
    """
    mandatory = ["byr",
                 "iyr",
                 "eyr",
                 "hgt",
                 "hcl",
                 "ecl",
                 "pid"]

    def contains(criteria, passport):
        for prop in passport.split(" "):
            prop_name = prop[0:3]
            if prop_name == criteria:
                return True
        return False

    for criteria in mandatory:
        if contains(criteria, passport) == False:
            return False
    return True


def validate(passports):
    nr_of_valid = 0
    for passport in passports:
        if is_valid_passport(passport):
            nr_of_valid += 1
    return nr_of_valid


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()
        passports = list(map(lambda passport: str(
            passport).replace("\n", " "), input.split("\n\n")))
        print(validate(passports))
