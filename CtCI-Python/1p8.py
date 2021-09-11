def zero_matrix(matrix):
    zero_pos = get_zp(matrix)
    consolidated_rows = get_cr(zero_pos)
    consolidated_cols = get_cc(zero_pos)
    
    for el in consolidated_rows:
        matrix[el] = [0]*len(matrix[el])
    
    for el in consolidated_cols:
        for i in range(len(matrix)):
            matrix[i][el] = 0
    return matrix

def get_zp(matrix):
    zero_pos = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_pos.append((i,j))
    return zero_pos


def get_cr(zero_pos):
    res = []
    for el in zero_pos:
        res.append(el[0])
    return set(res)


def get_cc(zero_pos):
    res = []
    for el in zero_pos:
        res.append(el[1])
    return set(res)

print(zero_matrix([[3,4,2,1,9], [2,1,4,1,0], [1,8,9,7,6]]))