n , m = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

square_sums = {}

for r in range(n - 1):
    for c in range(m - 1):
        current_square = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        square_sums[current_square] = [[matrix[r][c], matrix[r][c + 1]], [matrix[r + 1][c], matrix[r + 1][c + 1]]]

max_square = max(square_sums)

if max_square in square_sums:
    values = square_sums[max_square]
    for v in values:
        print(' '.join(str(x) for x in v))
print(max_square)
