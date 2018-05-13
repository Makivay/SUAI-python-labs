# 6. Дана последовательность ненулевых чисел. Определить, сколько раз в
# этой последовательности меняется знак (например, в
# последовательности {1, -34, 8, 14, -5} знак меняется 3 раза).


def lab5_var_6(data):
    count = 0  # кол-во смен знака
    for i in range(len(data) - 1):
        if data[i] == 0: raise ValueError("All values must be not null")
        first_sign = data[i] >= 0  # является ли предшевавствующий символ неотрицательным
        second_sign = data[i + 1] >= 0  # является ли текущий символ неотрицательным
        if first_sign != second_sign:
            count += 1
    return count


def test_lab5_var_6():
    print(lab5_var_6((1, 2)))
    print(lab5_var_6((1, -2)))
    print(lab5_var_6((1, 2, 3, -4, -5)))
    try:
        print(lab5_var_6((1, 0, 3, -4, -5)))
    except Exception as e:
        print('error: ' + repr(e))
    print(lab5_var_6((1, -34, 8, 14, -5)))


if __name__ == '__main__':
    test_lab5_var_6()
