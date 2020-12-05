import math

MAX_ROWS = 127  # Total: 128
MAX_SEATS = 7  # Total: 8


def get_row(seat_rows):
    min_row = 0
    max_row = MAX_ROWS

    for row in seat_rows:
        if row == 'F':
            max_row -= math.ceil((max_row - min_row) / 2)
        elif row == 'B':
            min_row += math.ceil((max_row - min_row) / 2)

    assert min_row == max_row
    return max_row


def get_seat_num(seat_nums):
    min_seat = 0
    max_seat = MAX_SEATS

    for num in seat_nums:
        if num == 'L':
            max_seat -= math.ceil((max_seat - min_seat) / 2)
        elif num == 'R':
            min_seat += math.ceil((max_seat - min_seat) / 2)

    assert min_seat == max_seat
    return max_seat


def get_seat_id(seat):
    row = get_row(seat[:7])
    seat_num = get_seat_num(seat[7:])

    return row * 8 + seat_num


with open("seats.txt", 'r') as file:
    seats = file.read().splitlines()

seat_ids = []

for seat in seats:
    seat_ids.append(get_seat_id(seat))

seat_ids.sort()

for i, seat in enumerate(seat_ids):
    if seat_ids[i + 1] != seat + 1:
        print(seat + 1)
        break


exit(0)
