def get_matrix():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix

matrix = get_matrix()
even_matrix = []

for r in matrix:
    even_matrix.append([x for x in r if x % 2 == 0])

print(even_matrix)