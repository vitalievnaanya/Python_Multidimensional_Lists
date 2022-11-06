def met_knight(board, row, col):
    if row < 0 or col < 0 or row >= len(board) or col >= len(board):
        return False
    return board[row][col] == 'K'


def met_knights(board, row, col):
    result = 0
    if met_knight(board, row - 2, col + 1):
        result += 1
    if met_knight(board, row - 2, col - 1):
        result += 1
    if met_knight(board, row + 2, col + 1):
        result += 1
    if met_knight(board, row + 2, col - 1):
        result += 1
    if met_knight(board, row + 1, col + 2):
        result += 1
    if met_knight(board, row + 1, col - 2):
        result += 1
    if met_knight(board, row - 1, col + 2):
        result += 1
    if met_knight(board, row - 1, col - 2):
        result += 1
    return result


n = int(input())

board = []

for _ in range(n):
    board.append(list(input()))

removed_knights = 0

while True:
    knight_count, row_position, col_position = 0, 0, 0
    for r in range(n):
        for c in range(n):
            if board[r][c] == '0':
                continue
            count = met_knights(board, r, c)
            if count > knight_count:
                knight_count, row_position, col_position = count, r, c
    if knight_count == 0:
        break
    board[row_position][col_position] = '0'
    removed_knights += 1

print(removed_knights)