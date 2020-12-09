

from collections import defaultdict


def count_declarations(groups, everyone_in_group=False):
    count = 0
    for group in groups:
        unique_yes = defaultdict(int)
        for person in group.splitlines():
            for char in person:
                unique_yes[char] += 1

        if everyone_in_group:
            for key in unique_yes.keys():
                # len(group.splitlines() == number of people in group
                if unique_yes[key] == len(group.splitlines()):
                    count += 1
        else:
            count += len(unique_yes)
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        groups = f.read().split("\n\n")
        resp = count_declarations(groups, True)
        print(resp)
