import warnings
import numpy as np
import functools
import matplotlib.pyplot as plt
from utils.math import factorial
from integrals.riemann_from_scratch import riemann_sum


def beta_distribution(x: float, alpha: float, beta: float) -> float:
    '''Beta distribution'''
    if x < 0 or x > 1:
        warnings.warn('x must be between 0 and 1')
        return 1
    return ((x ** (alpha - 1)) * ((1 - x) ** (beta - 1))) / ((factorial(alpha - 1) * factorial(beta - 1)) / factorial(alpha + beta - 1))


def plot_beta_distribution(success, failure, a, b):
    '''Plot the beta distribution'''
    fig, ax = plt.subplots()
    x = np.linspace(0, 1, 1000)
    y = [beta_distribution(i, success, failure) for i in x]
    ax.set_xlabel('Underlying rate of success')
    ax.set_ylabel(
        f'Likelihood of {success}/{success+failure} successes with a percentage of {a*100:.2f}%')
    plt.plot(x, y)
    plt.fill_between(x, y, where=(x >= a) & (x <= b), color='lightblue')
    plt.show()


def main():
    a = 0.9  # lower bound
    b = 1.0  # upper bound
    n = 10000  # precision of integral
    success = 8  # number of successes
    failure = 2  # number of failures
    greater_than = riemann_sum(n, a, b,
                               f=lambda x: beta_distribution(x, success, failure))  # integral of beta distribution from a to b
    print(f'With {success} successes and {failure} failures:')
    print(
        f'Probability of getting a score greater than {a*100:.2f}%: {greater_than}')
    print(
        f'Probability of getting a score less than {a*100:.2f}%: {1-greater_than}')
    plot_beta_distribution(success, failure, a, b)


if __name__ == '__main__':
    main()
