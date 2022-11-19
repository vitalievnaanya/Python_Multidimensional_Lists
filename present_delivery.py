def is_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n


def next_position(r, c, dir):
    if dir == 'up':
        return r - 1, c
    if dir == 'down':
        return r + 1, c
    if dir == 'right':
        return r, c + 1
    if dir == 'left':
        return r, c - 1


presents = int(input())

n = int(input())

neighborhood = []

for _ in range(n):
    neighborhood.append(input().split())

santa_row, santa_col = 0, 0
nice_kids = 0

for r in range(n):
    for c in range(n):
        if neighborhood[r][c] == 'S':
            santa_row, santa_col = r, c
        if neighborhood[r][c] == 'V':
            nice_kids += 1

kids_count = nice_kids

while True:
    command = input()

    if command == 'Christmas morning':
        break
    if presents == 0:
        break

    next_row, next_col = next_position(santa_row, santa_col, command)
    if is_valid(next_row, next_col, n):
        neighborhood[santa_row][santa_col] = '-'
        if neighborhood[next_row][next_col] == 'V':
            presents -= 1
            nice_kids -= 1
        if neighborhood[next_row][next_col] == 'C':

            if neighborhood[next_row - 1][next_col] != '-' and is_valid(next_row - 1, next_col, n):
                if neighborhood[next_row- 1][next_col] == 'V':
                    nice_kids -= 1
                presents -= 1
                neighborhood[next_row -1][next_col] = '-'
            if neighborhood[next_row + 1][next_col] != '-' and is_valid(next_row +1, next_col, n):
                if neighborhood[next_row + 1][next_col] == 'V':
                    nice_kids -= 1
                presents -= 1
                neighborhood[next_row + 1][next_col] = '-'
            if neighborhood[next_row][next_col - 1] != '-' and is_valid(next_row, next_col - 1, n):
                if neighborhood[next_row][next_col - 1] == 'V':
                    nice_kids -= 1
                presents -= 1
                neighborhood[next_row][next_col - 1] = '-'
            if neighborhood[next_row][next_col + 1] != '-' and is_valid(next_row, next_col + 1, n):
                if neighborhood[next_row][next_col + 1] == 'V':
                    nice_kids -= 1
                presents -= 1
                neighborhood[next_row][next_col + 1] = '-'

        neighborhood[next_row][next_col] = 'S'
        santa_row, santa_col = next_row, next_col

if presents == 0 and nice_kids > 0:
    print(f'Santa ran out of presents!')

for house in neighborhood:
    print(' '.join(house))

if nice_kids == 0:
    print(f'Good job, Santa! {kids_count} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids} nice kid/s.')
