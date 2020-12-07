ROWS = range(128)
ROW_SPLITS = 8
COLS = range(8)
COL_SPLITS = 3

DATA_SET = "datasets/day_5_puzzle_1.txt"


def puzzle_1():
    with open(DATA_SET, "r") as file:
        highest_seat_number = 0

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
            if seat > highest_seat_number:
                highest_seat_number = seat
            # print(f"ROW {final_row} * 8 + COL {final_col} = SEAT {seat}. Highest Seat: {highest_seat_number}")

        return highest_seat_number


if __name__ == "__main__":
    print(puzzle_1())
