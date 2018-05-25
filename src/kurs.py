def rotate(A, B, C):
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])


def jarvismarch(A):
    points_count = len(A)
    processing_indexes = range(points_count)
    # start point
    for i in range(1, points_count):
        if A[processing_indexes[i]][0] < A[processing_indexes[0]][0]:
            processing_indexes[i], processing_indexes[0] = processing_indexes[0], processing_indexes[i]
    result_indexes = [processing_indexes[0]]
    processing_indexes = [processing_indexes[i] for i in range(1, len(processing_indexes))]
    processing_indexes.append(result_indexes[0])
    while True:
        right = 0
        for i in range(1, len(processing_indexes)):
            if rotate(A[result_indexes[-1]], A[processing_indexes[right]], A[processing_indexes[i]]) < 0:
                right = i
        if processing_indexes[right] == result_indexes[0]:
            break
        else:
            result_indexes.append(processing_indexes[right])
            del processing_indexes[right]
    return result_indexes


if __name__ == '__main__':
    points = ((0, 0), (0, 2), (2, 0), (2, 2), (1, 1))
    print(jarvismarch(points))
