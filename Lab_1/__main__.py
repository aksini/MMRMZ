import math
import random
import matplotlib.pyplot as plt
import numpy as np

N = 1000


def draw(arrs, lines_label, dir_name, name):
    plt.figure()
    lines = plt.plot(*arrs)
    plt.legend(lines, lines_label)
    plt.savefig(f'Lab_1/{dir_name}/{name}.png')


def main_func(call):
    a = 4
    b = 13
    la = 2
    fi = 10
    q = 6
    dict_func = {
        '1': {
            'func': lambda start, finish: random.random() * (finish - start) + start,  #
            'args': [a, b],
            'name': 'interval'
        },
        '2': {
            'func': lambda lamb: math.log(random.random()) * (-1 / lamb),  #
            'args': [la],
            'name': 'exponential'
        },
        '3': {
            'func': lambda i, j: i + j * (sum([random.random() for _ in range(12)]) - 6),  #
            'args': [fi, q],
            'name': 'normal'
        }
    }
    selected = dict_func.get(call)
    func = selected.get('func')
    args = selected.get('args')
    name = selected.get('name')
    arr = []
    for _ in range(N+1):
        arr.append(func(*args))
    return arr, name


def math_exp(arr):
    m_exp = []
    for i in range(1, len(arr)+1):
        m_exp.append(np.mean(arr[:i]))
    return m_exp


def dispersion(arr, exp_arr):
    disp = []
    for i in range(1, len(arr)+1):
        try:
            d = sum([(item - exp_arr[i]) ** 2 for item in arr[:i]])
        except IndexError:
            continue
        disp.append(d / i)
    return disp


def error(arr_exp, arr_disp, name):
    L = 2
    Mt = (1 / L)
    Dt = (1 / (L * L))
    error_exp = []
    error_disp = []
    for exp, disp in zip(arr_exp, arr_disp):
        error_exp.append(abs(exp - Mt))
        error_disp.append(abs(disp - Dt))
    draw([range(len(arr_exp)), arr_exp, range(len(arr_disp)), arr_disp],
         ['mathematical expectation', 'dispersion'],
         name,
         'mathematical expectation and dispersion'
         )
    draw(
        [range(len(error_disp)), error_disp, range(len(error_exp)), error_exp],
        ['errors dispersions', 'errors mathematical expectation'],
        name,
        'errors of mathematical expectation and dispersion'
    )


def my_min(arr):
    min = arr[0]
    for i in arr[1:]:
        if min > i:
            min = i
    return min


def my_max(arr):
    max = arr[0]
    for i in arr[1:]:
        if max < i:
            max = i
    return max


def distribution(arr, name):
    k = 1 + int(round(3.2 * math.log10(N)))
    arr_max = my_max(arr)
    arr_min = my_min(arr)
    arr_kv = (arr_max - arr_min) / k
    arr_x = []
    arr_y = []
    data = [0 for item in range(k)]
    for i in arr:
        j = int((i - arr_min) / arr_kv)
        if j == k:
            j -= 1
        data[j] += 1

    for i in range(k):
        arr_x.append(arr_min + i * arr_kv)
        arr_y.append(data[i])
        i += 1

    fig, ax = plt.subplots(figsize=(15, 10), dpi=80)
    plt.bar(np.arange(len(arr_x)), arr_y, color='blue')
    ax.set_xticklabels(arr_x, horizontalalignment='left')
    plt.savefig(f'Lab_1/{name}/distribution.png')


if __name__ == '__main__':
    select = input(
        'Выберите одно из распределений:\n'
        '   1) На интервале [a,b]\n'
        '   2) Экспоненциальное\n'
        '   3) Нормальмальное \n'
    )
    array_exp, name_file = main_func(select)
    exp_math = math_exp(array_exp)
    exp_disp = dispersion(array_exp, exp_math)
    distribution(array_exp, name_file)
    error(exp_math, exp_disp, name_file)
    for i in [10, 20, 50, 100, 1000]:
        print(
            f'Значения для {i}\n'
            f'  Мат.ожидание {exp_math[i-1]}\n'
            f'  Дисперсия {exp_disp[i-1]}'
        )