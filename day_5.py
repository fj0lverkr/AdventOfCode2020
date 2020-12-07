ROWS = range(128)
ROW_SPLITS = 8
COLS = range(8)
COL_SPLITS = 3

DATA_SET = "datasets/day_5_puzzle_1.txt"


def puzzle(part: int):
    with open(DATA_SET, "r") as file:
        highest_seat_number = 0
        taken_seats = []

        for line in file.read().splitlines():
            rows = [n for n in ROWS]
            cols = [m for m in COLS]

            for i in range(ROW_SPLITS - 1):
                mid_row = int(len(rows) / 2)
                if line[i] == 'B':
                    rows = rows[mid_row:]
                else:
                    rows = rows[:mid_row]
            final_row = rows[0]

            for j in range(ROW_SPLITS - 1, ROW_SPLITS + COL_SPLITS - 1):
                mid_col = int(len(cols) / 2)
                if line[j] == 'R':
                    cols = cols[mid_col:]
                else:
                    cols = cols[:mid_col]
            final_col = cols[0]

            seat = final_row * 8 + final_col
            taken_seats.append(seat)
            if seat > highest_seat_number:
                highest_seat_number = seat
        if part == 1:
            return highest_seat_number
        elif part == 2:
            taken_seats.sort()
            your_seat = 0
            for k in range(len(taken_seats)):
                if taken_seats[k + 1] - taken_seats[k] > 1:
                    your_seat = taken_seats[k] + 1
                    break
            return your_seat


if __name__ == "__main__":
    print(puzzle(2))
