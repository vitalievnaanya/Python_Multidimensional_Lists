def is_inside(r, c, size):
    return 0 <= r < len(size) and 0 <= c < len(size)


n = int(input())

field = []

for _ in range(n):
    field.append(list(input().split()))

bunny_row = 0
bunny_col = 0

for r in range(n):
    for c in range(n):
        if field[r][c] == 'B':
            bunny_row, bunny_col = r, c

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

max_sum_eggs = 0
best_path = []
best_direction = ''

for direction, step in directions.items():
    eggs = 0
    path = []
    curr_row, curr_col = bunny_row, bunny_col

    while True:
        curr_row, curr_col = step(curr_row, curr_col)
        if not is_inside(curr_row, curr_col, field):
            break

        if field[curr_row][curr_col] == 'X':
            break

        eggs += int(field[curr_row][curr_col])
        path.append([curr_row, curr_col])

    if eggs > max_sum_eggs:
        max_sum_eggs = eggs
        best_path = path
        best_direction = direction


print(best_direction)
for path in best_path:
    print(path)
print(max_sum_eggs)