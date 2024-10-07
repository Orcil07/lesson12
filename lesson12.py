def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input(':'))
m = int(input(':'))
value = input(f': ')
print( * m)
matrix = get_matrix(n, m, value)

