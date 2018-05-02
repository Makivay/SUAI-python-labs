import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Интегральный закон распределения случайной величины
# распределенной по Гауссовскому закону
# мат модель http://profitraders.com/Math/Norm.html


def gaussian(lim_x, mu, sigma):
    """
        Parameters
        ----------
        lim_x : float
            предел интеграла
        mu : float
            среднее значение (мат.ожидание)
        sigma : float
            среднеквадратичное отклонение
    """
    return quad(lambda x: math.exp(-0.5 * ((x - mu) / sigma) ** 2), -np.inf, lim_x)[0] / sigma / math.sqrt(2 * math.pi)


def lab7_var_6(xs, mu, sigma):
    """
        Parameters
        ----------
        xs : iterable
            Сетка значений по оси абсцисс
        mu : float
            среднее значение (мат.ожидание)
        sigma : float
            среднеквадратичное отклонение
    """
    plt.plot(xs, [gaussian(x, mu, sigma) for x in xs], label='$\sigma = ' + str(sigma) + '$')
    plt.legend()
    plt.show()


def test_lab7_var_6():
    xs = np.arange(-8, 8, 0.05)
    lab7_var_6(xs, 0.0, 0.5)
    lab7_var_6(xs, 0.0, 1.0)
    lab7_var_6(xs, 0.0, 2.0)


if __name__ == '__main__':
    test_lab7_var_6()