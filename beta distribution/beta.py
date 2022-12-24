from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

nb_success = 748  # number of successes
nb_failure = 221  # number of failures
prc_goal = 0.8  # probability of reaching goal
# cumulative distribution function
p = beta.cdf(prc_goal, nb_success, nb_failure)
# for 8 successes and 2 failures:
# 0.7748409780000001 is the probability of getting 90% or less
# it is the area under the curve to the left of 0.9
print(p)

# plot beta distribution for 8 successes and 2 failures
fig, ax = plt.subplots()
x = np.linspace(beta.ppf(0, nb_success, nb_failure),
                beta.ppf(1, nb_success, nb_failure), 100)
ax.plot(x, beta.pdf(x, nb_success, nb_failure))
ax.set_ylabel("Likelihood")
ax.set_xlabel("Underlying rate of successes")
ax.yaxis.grid(True)
ax.xaxis.grid(True)
ax.set_axisbelow(True)
ax.set_title("Beta distribution")
plt.fill_between(x, beta.pdf(x, nb_success, nb_failure), where=x > prc_goal)
plt.text(prc_goal, 0, "Chance of {0}% or greater: {1:.2f}".format(
    prc_goal*100, 1-p), ha="center", va="bottom")
plt.xticks(np.arange(0, 1.1, 0.1))
plt.show()
