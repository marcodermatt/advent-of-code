def update_boards(boards, n):
    for board in boards:
        for row in board:
            for i, (val, _) in enumerate(row):
                if val == n:
                    row[i] = (val, True)

    return boards

def check_boards(boards):
    winning_boards = []
    for board in boards:
        if check_board(board):
            winning_boards.append(board)
    return winning_boards

def check_board(board):
    for i in range(5):
        if all([marked for _, marked in board[i]]):
            return True
        elif all([marked for _, marked in [row[i] for row in board]]):
            return True
    return False


def sum_unmarked(board):
    sum = 0
    for row in board:
        for val, marked in row:
            if not marked:
                sum += val
    return sum

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

drawn_numbers = list(map(int, data[0].split(',')))

i = 2
boards = []
while i < len(data):
    boards.append([list(map(lambda x: (int(x), False), data[i+r].split())) for r in range(5)])
    i += 6

for n in drawn_numbers:
    boards = update_boards(boards, n)
    win_board = check_boards(boards)
    if len(win_board) > 0:
        for entry in win_board:
            print(entry)
            boards.remove(entry)
        if len(boards) == 0:
            print(n)
            print(sum_unmarked(win_board[0])*n)
            break
