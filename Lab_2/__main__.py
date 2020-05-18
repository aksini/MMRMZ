from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np


def draw(arrs, lines_label, dir_name, name):
    plt.figure()
    lines = plt.plot(*arrs)
    plt.legend(lines, lines_label, loc='upper center')
    plt.xlabel('Интервал значений от 0.0 до 10.0')
    plt.savefig(f'Lab_2/{dir_name}/{name}.png')


def func_integ(x):
    return 1 / (x**2 + x - 2)


def func_integ_romb(y):
    return 1 / (y**2 + y - 2)


def func_diff(y, t):
    v, x = y
    f0 = 3 * x
    f1 = v
    return [f0, f1]


def acc_sol(t):
    return np.exp(np.sqrt(3) * t) + 1 / np.exp(np.sqrt(3) * t)


def integration(start_, finish_):
    x = np.arange(start_, finish_, 0.5)
    y = np.arange(start_, finish_, 0.6)
    quad_result = integrate.quad(func_integ, start_, finish_)
    trapz_result = integrate.trapz(1 / (x * x + x - 2), x)
    simps_result = integrate.simps(1 / (x * x + x - 2), x)
    romb_result = integrate.romb(func_integ_romb(y), show=True)
    print("Точное решение: ", quad_result[0])
    print('Точность вычисления: ', quad_result[1])
    print('Метод трапеции = %f' % trapz_result)
    print('Метод Симпсона = %f' % simps_result)
    print('Метод Ромберга = %f' % romb_result)


def differentiation():
    t = np.linspace(0, 10, 100)
    v0 = 0.
    x0 = 1.
    y0 = (v0, x0)
    diff_result = integrate.odeint(func_diff, y0, t)
    diff_error = acc_sol(t) - diff_result[:, 1]
    print('Численное решение ОДУ: ', diff_result)
    # print('Точное решение ОДУ: ', *acc_sol(t))
    # print('Относительная погрешность: ', *diff_error)
    draw([t, diff_result[:, 1], t, acc_sol(t)],
         ['Численное решение', 'Точное решение'],
         'differentiation',
         'diff')
    draw([t, diff_error],
         ['Относительная погрешность'],
         'differentiation',
         'error_diff')


if __name__ == '__main__':
    start = -1.9
    finish = 0.9
    integration(start, finish)
    differentiation()
