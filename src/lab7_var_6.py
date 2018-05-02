import math

import matplotlib.pyplot as plt
import numpy as np
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
    plt.plot(xs, [gaussian(x, mu, sigma) for x in xs],
             label='$\mu = ' + "%.1f" % mu + ', \sigma^2 = ' + "%.1f" % (sigma ** 2) + '$')


def test_lab7_var_6():
    xs = np.arange(-5, 5, 0.01)
    lab7_var_6(xs, 0.0, math.sqrt(0.2))
    lab7_var_6(xs, 0.0, math.sqrt(1.0))
    lab7_var_6(xs, 0.0, math.sqrt(5.0))
    lab7_var_6(xs, -2.0, math.sqrt(0.5))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    test_lab7_var_6()
