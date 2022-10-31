n = int(input())

matrix = []
m = 0

for _ in range(n):
    row = input()
    matrix.append(row)

searched_symbol = input()
is_found = False
row, col = None, None

for r in range(len(matrix)):
    if is_found:
        break
    for c in range(len(matrix[r])):
        if matrix[r][c] == searched_symbol:
            row, col = r, c
            is_found = True
            break

if is_found:
    print(f'({row}, {col})')
else:
    print(f'{searched_symbol} does not occur in the matrix')