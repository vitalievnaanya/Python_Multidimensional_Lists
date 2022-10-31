n, m =[int(x) for x in input().split(', ')]

matrix = []

for _ in range(n):
    row =[int(x) for x in input().split()]
    matrix.append(row)

for c in range(m):
    column_sum = 0
    for r in range(n):
        column_sum += matrix[r][c]
    print(column_sum)