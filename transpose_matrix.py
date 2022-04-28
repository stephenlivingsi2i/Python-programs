mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

result_matrix = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        result_matrix[j][i] = mat[i][j]

for x in result_matrix:
    print(x)
