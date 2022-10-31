n, m = [int(x) for x in input().split(', ')]

matrix = []
sum_of_matrix = 0

for r in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    sum_of_matrix += sum(row)

print(sum_of_matrix)
print(matrix)