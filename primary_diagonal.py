n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_diagonal = []

for r in range(n):
    primary_diagonal.append(matrix[r][r])

print(sum(primary_diagonal))