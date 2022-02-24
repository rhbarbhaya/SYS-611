"""
Example: Validation of the Dice Rollers data set.

@author: Paul T. Grogan <pgrogan@stevens.edu>
"""

# import the pandas package and refer to it as `pd`
# see http://pandas.pydata.org/pandas-docs/stable/ for documentation
import pandas as pd

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# import the matplotlib pyplot package and refer to it as `plt`
# see http://matplotlib.org/api/pyplot_api.html for documentation
import matplotlib.pyplot as plt

# import the scipy stats package and refer to it as `stats`
# see http://docs.scipy.org/doc/scipy/reference/stats.html for documentation
import scipy.stats as stats

# read data file
df = pd.read_csv('roller.csv')

# generate labels for discrete values (number of hits in 10 dice rolls)
labels = ["0-4", "5", "6", "7", "8", "9", "10"]
# generate indices for discrete values
indices = np.arange(len(labels))
# list the observed count for each value - append 0-4 (aggregated) and 5-10
observed = np.append(np.sum(df['How many hits did you roll?'] <= 4), 
                     [np.sum(df['How many hits did you roll?'] == i) for i in range(5,11)])
# list the expected count for each value using binomial distribution with
# n=10 trials and p=2/3 chance for success in each trial
# append the cdf aggregating 0-3 and the pdf for other values 4-10
# and multiply by the total number of observations
expected = np.append(
    stats.binom.cdf([4], 10, 2./3), 
    stats.binom.pmf([5, 6, 7, 8, 9, 10], 10, 2./3)
)*np.sum(observed)

# create a new bar chart to display the observed and expected values
plt.figure()
plt.bar(indices-0.2, observed, 0.4, color='b', label="Observed")
plt.bar(indices+0.2, expected, 0.4, color='k', label="Expected")
plt.xlabel("Number Hits (X)")
plt.ylabel("Count")
plt.xticks(indices, labels)
plt.legend(loc="best")

# perform a one-way chi-squared test and print the statistic and p-value
t, p = stats.chisquare(observed, expected)
print "t = {:.2f}".format(t)
print "p = {:.4f}".format(p)

# generate a linear space between 0 and 30 for possible statistic values
t_vars = np.linspace(0,30)
# record the degrees of freedom (6)
degrees_freedom = np.size(observed)-1

# list desired alpha level
alpha = 0.05
# compute and print critical statistic value
t_crit = stats.chi2.ppf(1-alpha, degrees_freedom)
print "critical chi^2_6 = {:.2f}".format(t_crit)

# create a plot to show chi-squared CDF with resulting and critical statistics
plt.figure()
plt.plot(t_vars, stats.chi2.cdf(t_vars, degrees_freedom), '-b', label="$\chi^2_6$")
plt.plot([t, t], [0, 1], 'r', label="$t$")
plt.plot([t_crit, t_crit], [0, 1], '-g', label="$t_{crit}$")
plt.title('Plot of $\chi^2_6$ CDF with critical and observed statistics')
plt.xlabel("$t$")
plt.ylabel("$F(t)=P\{T<t\}$")
plt.legend(loc='best')