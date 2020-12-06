
import math
from types import resolve_bases


def get_seat_id(seat_code):
    row = get_row(seat_code[0:7])
    col = get_col(seat_code[7:])
    return (row*8) + col


def get_row(row_code, iteration=0, low=0, high=127):
    if len(row_code) == iteration:
        return high if row_code[-1] == "F" else low

    code = row_code[iteration]
    mid = math.ceil(abs(high-low)/2)
    if code == "F":
        return get_row(row_code, iteration+1, low, high-mid)
    else:
        return get_row(row_code, iteration+1, low+mid, high)


def get_col(col_code, iteration=0, low=0, high=7):
    if len(col_code) == iteration:
        return high if col_code[-1] == "L" else low

    code = col_code[iteration]
    mid = math.ceil(abs(high-low)/2)
    if code == "L":
        return get_col(col_code, iteration+1, low, high-mid)
    else:
        return get_col(col_code, iteration+1, low+mid, high)


def get_highest_seat(seat_data):
    seat_ids = []
    for seat in seat_data:
        seat_ids.append(get_seat_id(seat))

    seat_ids.sort(reverse=True)
    return seat_ids[0]


def get_my_seat(seat_data):
    seats = []
    for seat in seat_data:
        row = get_row(seat[0:7])
        if row > 0 and row < 127:
            seats.append(get_seat_id(seat))

    seats.sort()
    for index, seat in enumerate(seats):
        if index > 0 and index < len(seats):
            before = seats[index-1]
            after = seats[index+1]
            if abs(after - before) > 2:
                if abs(seats[index] - before) > 2:
                    return seats[index]-1
                else:
                    return seats[index]+1


if __name__ == "__main__":
    seat_data = []
    with open("input.txt") as file:
        seat_data = file.read().splitlines()
    print(get_highest_seat(seat_data))
    print(get_my_seat(seat_data))
