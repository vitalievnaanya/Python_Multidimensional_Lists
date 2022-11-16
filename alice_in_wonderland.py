def is_valid(r, c, size):
    return 0 <= r < len(size) and 0 <= c < len(size)


def next_position(cmd, r, c):
    if cmd == 'up':
        return r - 1, c
    if cmd == 'down':
        return r + 1, c
    if cmd == 'left':
        return r, c - 1
    if cmd == 'right':
        return r, c + 1


n = int(input())

territory = []

for _ in range(n):
    territory.append(input().split())


alice_row, alice_col = 0, 0

for r in range(n):
    for c in range(n):
        if territory[r][c] == 'A':
            alice_row, alice_col = r, c
            territory[alice_row][alice_col] = '*'

collected_tea = 0

while True:
    command = input()
    alice_row, alice_col = next_position(command, alice_row, alice_col)
    cell_value = territory[alice_row][alice_col]

    if cell_value.isdigit():
        collected_tea += int(cell_value)
        if collected_tea >= 10:
            territory[alice_row][alice_col] = '*'
            break
    if not is_valid:
        break
    if territory[alice_row][alice_col] == 'R':
        territory[alice_row][alice_col] = '*'
        break
    territory[alice_row][alice_col] = '*'

if collected_tea >= 10:
    print(f'She did it! She went to the party.')
else:
    print(f"Alice didn't make it to the tea party.")

for part in territory:
    print(' '.join(str(x) for x in part))
