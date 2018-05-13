import random


# 6. Задана матрица. Вычислите ее определитель методом разложения по
# строке (столбцу).

def rand10(): return int(random.random() * 10)


def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print(str(matrix[x][y]) + ' ', end="")
        print()


def get_submatrix(matrix, except_x, except_y):
    return [
        [
            matrix[x][y]
            for y in range(len(matrix[x])) if y not in [except_y]
        ]
        for x in range(len(matrix)) if x not in [except_x]
    ]


def determinant(matrix):
    lenght = len(matrix)
    if lenght == 0:
        return 0
    elif lenght == 1:
        return matrix[0][0]
    elif lenght == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        amount = 0
        x = 0  # better use line with maximum zeroes
        for y in range(len(matrix)):
            submatrix = get_submatrix(matrix, x, y)
            if y % 2 == 0:
                amount += matrix[x][y] * determinant(submatrix)
            else:
                amount -= matrix[x][y] * determinant(submatrix)
        return amount


def lab6_var_6(size):
    matrix = [[rand10() for x in range(size)] for y in range(size)]
    print_matrix(matrix)
    return determinant(matrix)


def test_lab6_var_6():
    print(lab6_var_6(0))
    print(lab6_var_6(1))
    print(lab6_var_6(2))
    print(lab6_var_6(3))


if __name__ == '__main__':
    test_lab6_var_6()
