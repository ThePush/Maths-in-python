from scipy.stats import binom
import matplotlib.pyplot as plt

nb_trials = 10  # number of trials
p_success = 0.9  # probability of success

for k in range(nb_trials + 1):  # k: number of successes
    # probability mass function
    probability = binom.pmf(k, nb_trials, p_success)
    print("{0} - {1}".format(k, probability))

print("Mean: {0}".format(binom.mean(nb_trials, p_success)))
print("Variance: {0}".format(binom.var(nb_trials, p_success)))
print("Probability of p given n: {0}".format(
    binom.pmf(p_success*10, nb_trials, p_success)))

fig, ax = plt.subplots()
plot = ax.bar(range(nb_trials + 1),
              binom.pmf(range(nb_trials + 1), nb_trials, p_success))
ax.set_ylabel("Probability of {0}% success rate".format(p_success*100))
ax.set_xlabel("Number of successes with {0} trials".format(nb_trials))
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.set_title("Binomial distribution")
for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2.0, height,
            "{0:.2f}".format(height), ha="center", va="bottom")
    plt.xticks(range(nb_trials + 1))
plt.show()

# https://www.geeksforgeeks.org/python-binomial-distribution/
