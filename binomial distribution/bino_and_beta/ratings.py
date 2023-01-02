from scipy.stats import binom
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

# nb_ratings = 1005  # number of ratings
# score = 4.75  # score of all ratings
# positive_ratings = 784  # number of positive ratings
# negative_ratings = 221  # number of negative ratings

nb_ratings = 10  # number of ratings
score = 4  # score of all ratings
positive_ratings = 8  # number of positive ratings
negative_ratings = 2  # number of negative ratings

###############################################################################
############################ BINOMIAL DISTRIBUTION ############################
###############################################################################

# laplace smoothing: add 2 rating to the score, 1 positive and 1 negative
nb_ratings += 2
smoothed_goal = ((score * (nb_ratings-2)) + 5.0 + 1.0) / (nb_ratings)
print("Smoothed goal: {0}".format(smoothed_goal))
# normalize smoothed_goal to 0-1
smoothed_goal *= 0.2

# for k in range(nb_ratings + 1):  # k: number of successes
#    # probability mass function
#    probability = binom.pmf(k, nb_ratings, smoothed_goal)
#    print("{0} - {1}".format(k, probability))

print("Binomial:\nProbability of having at least {0:.2f} stars with {1} ratings and a mean of {2:.2f}: {3:.2f}%".format(
    score, nb_ratings-2, score, binom.sf(smoothed_goal/.2, nb_ratings, smoothed_goal)*100))

fig, ax = plt.subplots()
plot = ax.bar(range(nb_ratings + 1),
              binom.pmf(range(nb_ratings + 1), nb_ratings, smoothed_goal))
ax.set_ylabel("Probability of {0:.2f} stars".format(score))
ax.set_xlabel("Number of successes with {0} ratings".format(nb_ratings-1))
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.set_title("Binomial distribution")
# for rect in plot:
#    height = rect.get_height()
#    ax.text(rect.get_x() + rect.get_width()/2.0, height,
#            "{0:.2f}".format(height), ha="center", va="bottom")
plt.xticks(range(nb_ratings + 1))
plt.show()


###############################################################################
############################# BETA DISTRIBUTION ###############################
###############################################################################

# laplace smoothing: add 1 positive rating and 1 negative rating
positive_ratings += 1
negative_ratings += 1

p = beta.cdf(smoothed_goal, positive_ratings, negative_ratings)
print(p)
# for 8 successes and 2 failures:
# 0.7748409780000001 is the probability of getting 90% or less
# it is the area under the curve to the left of 0.9
print("Beta:\nProbability of having at least {0:.2f} stars with {1} positive ratings and {2} negative ratings: {3:.2f}%".format(
    score, positive_ratings-1, negative_ratings-1, (1-p)*100))

# plot beta distribution for 8 successes and 2 failures
fig, ax = plt.subplots()
x = np.linspace(beta.ppf(0, positive_ratings, negative_ratings),
                beta.ppf(1, positive_ratings, negative_ratings), 100)
ax.plot(x, beta.pdf(x, positive_ratings, negative_ratings))
ax.set_ylabel("Likelihood")
ax.set_xlabel("Underlying rate of successes")
ax.yaxis.grid(True)
ax.xaxis.grid(True)
ax.set_axisbelow(True)
ax.set_title("Beta distribution")
plt.fill_between(x, beta.pdf(x, positive_ratings,
                 negative_ratings), where=x > 1-p)
plt.text(smoothed_goal, 0, "Chance of {0} stars or greater: {1:.2f}".format(
    score, 1-p), ha="center", va="bottom")
plt.xticks(np.arange(0, 1.1, 0.1))
plt.axline((1-p, 0), (1-p, 1), color="red")
plt.show()
