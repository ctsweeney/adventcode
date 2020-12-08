def read_boarding_pass_file(raw) -> list:
    with open(raw) as pp:
        boardingpass_data = pp.read()
        fmt_data = boardingpass_data.split("\n")
        return fmt_data


def check_boarding_row(data):
    # Check Row
    row = 0
    for r in range(7):
        if data[r] == "B":
            row += 1 << (6 - r)
    # Check columns
    col = 0
    for c in range(3):
        if data[c + 7] == "R":
            col += 1 << (2 - c)

    # Calclate seat number
    return row * 8 + col


boarding_pass = read_boarding_pass_file('data.txt')

maxID = 0

for p in boarding_pass:
    print(maxID)
    maxID = max(maxID, check_boarding_row(p))

print(maxID)
