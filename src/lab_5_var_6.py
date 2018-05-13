# 6. Дана последовательность ненулевых чисел. Определить, сколько раз в
# этой последовательности меняется знак (например, в
# последовательности {1, -34, 8, 14, -5} знак меняется 3 раза).


def lab5_var_6(data):
    count = 0
    for i in range(len(data) - 1):
        val1 = data[i] >= 0
        val2 = data[i + 1] >= 0
        if val1 != val2:
            count += 1
    return count


def test_lab5_var_6():
    print(lab5_var_6((1, 2)))
    print(lab5_var_6((1, -2)))
    print(lab5_var_6((1, -2, 3, -4, 5)))


if __name__ == '__main__':
    test_lab5_var_6()