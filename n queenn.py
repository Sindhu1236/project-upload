'''def is_safe(board, row, col, num):

    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    startrow = row - row % 3
    startcol = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[startrow + i][startcol + j] == num:
                return False

    return True


def solve(board, row, col):

    if row == 9:
        return True

    if col == 9:
        return solve(board, row + 1, 0)

    if board[row][col] != 0:
        return solve(board, row, col + 1)

    for num in range(1, 10):

        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve(board, row, col + 1):
                return True

            board[row][col] = 0

    return False


board = []

for i in range(9):
    board.append(list(map(int, input().split())))

if solve(board, 0, 0):
    for row in board:
        print(row)
else:
    print("No solution")'''
def is_safe(board, row, col, num):

    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    startrow = row - row % 3
    startcol = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[startrow + i][startcol + j] == num:
                return False

    return True


def solve(board, row, col):

    if row == 9:
        return True

    if col == 9:
        return solve(board, row + 1, 0)

    if board[row][col] != 0:
        return solve(board, row, col + 1)

    for num in range(1, 10):

        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve(board, row, col + 1):
                return True

            board[row][col] = 0

    return False


board = []

for i in range(9):
    board.append(list(map(int, input().split())))

if solve(board, 0, 0):
    for row in board:
        print(row)
else:
    print("No solution")