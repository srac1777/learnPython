def rotate_matrix(matrix):
    transpose_matrix(matrix)
    return reverse_rows(matrix)

def transpose_matrix(matrix):
    # print(matrix)
    for i in range(0, len(matrix)-1):
        for j in range(i+1, len(matrix)):
            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t
    # print(matrix)

def reverse_rows(matrix):
    for i in range(len(matrix)):
        arr = matrix[i]
        for j in range(0, int(len(arr)/2)):
            t = arr[j]
            arr[j] = arr[-j-1]
            arr[-j-1] = t
    return matrix


print(rotate_matrix([['a', 'b', 'c', ], ['d', 'e', 'f'], ['g', 'h', 'i']]))
