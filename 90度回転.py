def rotate_clockwise(matrix):
    transposed_matrix = zip(*matrix[::-1])
    return list(map(list, transposed_matrix))
