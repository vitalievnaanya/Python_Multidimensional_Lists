def is_valid(r, c, rs):
    if r >= 0 and c >= 0 and (r <= rs - 1) and (c <= rs - 1):
        return True
    return False


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

data = input()

while data != 'END':
    data = data.split()
    command = data[0]
    row, col, value = [int(x) for x in data[1:]]
    if is_valid(row, col, rows):
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print(f'Invalid coordinates')

    data = input()

for row in matrix:
    print(' '.join(str(x) for x in row))