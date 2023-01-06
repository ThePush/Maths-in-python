# Riemman's sum
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import inspect


def riemann_sum(n, a, b, f):
    '''Riemann's sum:
    n = number of rectangles
    a = lower bound
    b = upper bound
    f = function'''
    w = (b - a) / n  # width of rectangles
    res = 0  # return value
    k = 1  # counter
    for k in range(1, n + 1):
        res += w * f(a + k * w) # add the area of the rectangle: width * height(=f(xi))
    return res


def function_as_string(f):
    '''Return the function as a string'''
    source = inspect.getsource(f)  # get the source code of the function
    return_string = source.split('return')[-1]  # get the string after 'return'
    return_string = return_string.strip()  # remove leading and trailing spaces
    return_string = return_string.split('#')[0]  # remove the comment
    return_string = return_string.replace('**', '^')
    return_string = return_string.replace('*', '')
    return_string = '$' + return_string + '$'  # add LaTeX math mode
    return return_string


def plot_integrals(n, a, b, f):
    '''Plot the function with the rectangles under the curve'''
    fig, ax = plt.subplots()
    x = np.linspace(a, b, 1000)
    y = f(x)
    ax.plot(x, y, 'r')

    text = 'Riemann sum: ' + \
        str(riemann_sum(n, a, b, f)) + '\nNumber of rectangles: ' + str(n)
    ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=12, verticalalignment='top')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)', rotation=0)
    title = 'Riemann sum of function $f(x)$: ' + function_as_string(
        f) + '\nRange: [' + '{:.2f}'.format(a) + ', ' + '{:.2f}'.format(b) + ']'
    ax.set_title(title)

    rect_width = (b - a) / n
    for i in range(n):
        left_x = a + i * rect_width
        rect_height = f(left_x)
        rect = Rectangle((left_x, 0), rect_width,
                         rect_height, color='b', alpha=0.2)
        ax.add_patch(rect)

    plt.show()


def main():
    n = 12  # number of rectangles under the curve
    a = -1  # lower bound
    b = 4  # upper bound
    def f(x): return x**3 - 5*x**2 + x + 10  # function to integrate
    plot_integrals(n, a, b, f)


if __name__ == '__main__':
    main()
