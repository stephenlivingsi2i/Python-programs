first_matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

second_matrix = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]

result_matrix = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

for i in range(len(first_matrix)):
    # iterate through columns of Y
    for j in range(len(second_matrix[0])):
        # iterate through rows of Y
        for k in range(len(second_matrix)):
            result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]

for r in result_matrix:
    print(r)