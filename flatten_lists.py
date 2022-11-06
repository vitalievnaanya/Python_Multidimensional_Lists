given_list = input().split('|')

matrix = []

for el in given_list:
    elements = el.split()
    matrix.append(elements)

reversed_matrix = []

for _ in range(len(matrix)):
    reversed_matrix.append(matrix.pop())

for row in reversed_matrix:
    print(' '.join(row) ,end=' ')