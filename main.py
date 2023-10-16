import sympy
from sympy import Symbol
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

_ = ('lab number 4')
print(_.center(40))
f = sympy.sympify(input('Enter your function: '))

xs = Symbol('x')


def func(x):
    k = Symbol('x')
    return f.subs(k, x)


a = int(input('a = '))
b = float(input('b = '))
N = int(input('Number of steps: '))


def Formula_of_rectangles(a1, b1, n):
    sum = 0
    h = (b1 - a1) / n
    i = 1
    while i <= n:
        sum += func(a1 + (0.5 * h))
        a1 += h
        i += 1
    return h * sum


def Formula_of_trapezoids(a1, b1, n):
    h = (b1 - a1) / n
    i = 1
    sum = 0
    sum1 = h / 2 * (func(a1) + func(b1))
    while i <= n - 1:
        sum += func(a1 + h)
        a1 += h
        i += 1
    return h * sum + sum1


def Formula_of_parabola(a1, b1, n):
    sum_even = 0
    sum_no_even = 0
    h = (b1 - a1) / n
    i = 1
    sum1 = func(a1) + func(b1)
    while i <= n:
        if i % 2 != 0:
            sum_no_even += func(a1 + h)
            a1 += h
        if i % 2 == 0 and i != n:
            sum_even += func(a1 + h)
            a1 += h
        i += 1
    return (h / 3) * (4 * sum_no_even + 2 * sum_even + sum1)


def Formula_of_Gauss(a1, b1):
    return ((b1 - a1) / 2) * (
            func((a1 + b1) / 2 - (b1 - a1) / (2 * sqrt(3))) + func((a1 + b1) / 2 + (b1 - a1) / (2 * sqrt(3))))


t_arr4 = [-0.861136, -0.339981, 0.339981, 0.861136]
c_arr4 = [0.347855, 0.652145, 0.652145, 0.347855]
'''t_arr5 = [-0.90618, -0.538469, 0, 0.538469, 0.90618]
c_arr5 = [0.23693, 0.47863, 0.56889, 0.47863, 0.23693]'''


def Formula_of_Gauss2(f1, sym, a1, b1, e1, t_arr, c_arr):
    if (b1 - a1) / 4 > e1:
        n = 4
        delta = (b1 - a1) / n
        return sum(list(
            [Formula_of_Gauss2(f1, sym, a1 + delta * i, a1 + delta * (i + 1), e1, t_arr, c_arr) for i in range(n)]))

    else:
        if len(t_arr) == len(c_arr):
            t_arr = [t_arr[i] + abs(a1 - b1) / 2 for i in range(len(t_arr))]
            arr = []
            for i in range(len(t_arr)):
                xi = (b1 + a1) / 2 + (b1 - a1) * t_arr[i] / 2
                arr.append(c_arr[i] * f1.evalf(subs={sym: xi}))

            return (b1 - a1) / 2 * sum(arr)


print('Formula_of_rectangles:', round(Formula_of_rectangles(a, b, N), 5))
print('Formula_of_trapezoids:', round(Formula_of_trapezoids(a, b, N), 5))
print('Formula_of_parabola:', round(Formula_of_parabola(a, b, N), 5))
print('Formula_of_Gauss:', round(Formula_of_Gauss(a, b), 5))
print('Formula_of_Gauss2:', round(Formula_of_Gauss2(f, xs, a, b, 0.01, t_arr4, c_arr4), 2))


def graph(a1, b1):
    arr = []
    while a1 <= b1:
        arr.append(a1)
        a1 += 1
    return (arr)


x = np.linspace(a, b)
y = []
for i in x:
    y.append(func(i))
_2 = 'y = ' + str(f)
plt.title(_2)
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.plot(x, y, color='yellow')
plt.plot([a, a], [0, func(a)], color='red')
plt.plot([b, b], [0, func(b)], color='red')
plt.plot([a, b], [0, 0], color='red')
plt.grid()
plt.show()
'''    if (b1 - a1) / 4 > 0.01:
        n = 4
        delta = (b1 - a1) / n
        return sum(list([gauss(f1, a + delta*i, a + delta*(i+1), e1, t_arr, c_arr) for i in range(n)]))

    else:'''
'''x_ = []
for i in x:
    x_.append(i)
x_2 = [a, b, a, b]
y_2 = [0, 0, func(a), func(b)]
plt.fill(x_, y, x_2, y_2)'''
