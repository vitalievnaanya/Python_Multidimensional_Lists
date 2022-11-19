def is_valid(r, c):
    if 0 <= r < 5 and 0 <= c < 5:
        return r, c


def next_move(r, c, n, dir):
    if dir == 'up':
        return r - n, c
    if dir == 'down':
        return r + n, c
    if dir == 'left':
        return r, c - n
    if dir == 'right':
        return r, c + n


field = []

for _ in range(5):
    field.append(input().split())

targets = 0
row, col = 0, 0

for r in range(5):
    for c in range(5):
        if field[r][c] == 'x':
            targets += 1
        if field[r][c] == 'A':
            row, col = r, c

n = int(input())
next_row, next_col = 0, 0

shooting_dir = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
}

hit_targets = []

for _ in range(n):
    command = input().split()
    direction = command[1]

    if command[0] == 'move':
        steps = int(command[2])

        next_row, next_col = next_move(row, col, steps, direction)
        if is_valid(next_row, next_col):
            if field[next_row][next_col] != 'X':
                field[next_row][next_col] = 'A'
                field[row][col] = '.'
                row, col = next_row, next_col
        else:
            next_row, next_col = 0, 0
            continue

    else:
        step = shooting_dir[direction]
        bullet_row, bullet_col = step(row, col)
        while True:
            if is_valid(bullet_row, bullet_col):
                if field[bullet_row][bullet_col] == 'x':
                    hit_targets.append([bullet_row, bullet_col])
                    field[bullet_row][bullet_col] = '.'
                bullet_row, bullet_col = step(bullet_row, bullet_col)
            if not is_valid(bullet_row, bullet_col):
                break

        if len(hit_targets) == targets:
            break
if len(hit_targets) == targets:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets - len(hit_targets)} targets left.")

for target in hit_targets:
    print(target)
