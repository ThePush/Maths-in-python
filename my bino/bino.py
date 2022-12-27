import warnings
import numpy as np
import functools
import matplotlib.pyplot as plt

# n: number of experiments
# k: number of successes
# p: probability of success
# q: probability of failure

# function:
# p(X = k) = n! / (k! * (n - k)!) * p^k * q^(n - k)


# @functools.cache
def factorial(n):
    for i in range(1, n):
        n *= i
    if n == 0:
        return 1
    return n
    # return n * factorial(n - 1) if n else 1


def binomial(n, k, p):
    '''Binomial distribution'''
    # product of possible combinations of k successes in n experiments * probability of k successes * probability of failures
    return (factorial(n) / (factorial(k) * factorial(n - k))) * (p**k * (1 - p)**(n - k))


# def normalize_rating(rating, min_rating, max_rating):
#    '''Normalize rating to 0-1'''
#    return (rating - min_rating) / (max_rating - min_rating)


def plot_binomial(n, p):
    fig, ax = plt.subplots()

    x = np.arange(n+1)
    y = np.array([binomial(n, k, p) for k in range(n+1)])
    y = np.ma.masked_where(y < 0.001, y)

    for i, j in zip(x, y):
        if not np.isnan(j):
            ax.annotate(f'{j:.4f}', xy=(i, j), ha='center', va='bottom')
    ax.set_ylim(0, 1)
    ax.bar(x, y, align='center', width=0.5)
    ax.set_ylabel(f'Probability of {p*100:.2f}% success rate')
    ax.set_xlabel(f'Number of successes with {n} trials')
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)
    ax.set_title("Binomial distribution")

    plt.show()


def main():
    # score = 4  # score of all ratings
    # n = 0  # number of experiments
    # k = 0  # number of positive ratings
    # q = n - k  # number of negative ratings
    # p = 0.9  # probability of success

    while True:
        n = int(input('Number of experiments: '))
        k = int(input('Number of successes: '))
        n += 2  # laplace smoothing
        k += 1  # laplace smoothing
        print(f'Percentage of success after smoothing: {k/n*100:.2f}%')
        print(
            f'Bernoulli distribution of {k/n*100:.2f}% success rate: {binomial(n, k, k/n)} at {k} successes in {n} trials')
        print(
            f'Plotting binomial distribution of {k/n*100:.2f}% success rate...')
        plot_binomial(n, k/n)


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    main()

# n: number of experiments
# k: number of successes
# p: probability of success
# q: probability of failure