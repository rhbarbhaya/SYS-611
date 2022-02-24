"""
Example: Validation of the Human RNG data set.

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
df = pd.read_csv('rng.csv')
# extract the values column and sort in ascending order
values = np.sort(df['Enter a random floating-point number between 0 and 1.'])
# define a cdf generator to count the fraction of values below a level x
values_cdf = [np.sum(values <= x)/float(len(values)) for x in values]

# set the random seed to zero for consistent results
np.random.seed(0)
# generate an equivalent list of random numbers and sort in ascending order
rng = np.sort(np.random.rand(len(values)))
# define a cdf function to count the fraction of values below a level x
rng_cdf = [np.sum(values <= x)/float(len(values)) for x in values]

# define an expected cdf based on the theoretical uniform distribution
expected_cdf = lambda x: x

#%%

# plot a histogram of the two samples, overlay the expected counts
plt.figure()
plt.hist([values, rng], label=['Human', 'Numpy'], color=['b', 'k'])
plt.plot([0, 1], [.1*len(values), .1*len(values)], '-r', label='Expected')
plt.xlabel('X Bin')
plt.ylabel('Count')
plt.legend(loc='best')

#%%

# plot the observed CDFs and expected CDF
plt.figure()
plot_x = np.linspace(0,1)
plt.plot(plot_x, [expected_cdf(x) for x in plot_x], '-r', label='$F(x)$')
plt.step(values, values_cdf, '-b', where='post', label='$F_n(x)$ Human')
plt.xlabel('$x$')
plt.ylabel('$P\{X \leq x\}$')
plt.legend(loc='best')

# compute the k-s statistic using a formula
k_values = np.max(np.abs(np.subtract(
        values_cdf, [expected_cdf(x) for x in values])))

# print the results of the scipy.stats k-s test
print stats.kstest(values, lambda x: x)

#%% comparative analysis for numpy rng

# plot the observed CDFs and expected CDF
plt.figure()
plot_x = np.linspace(0,1)
plt.plot(plot_x, [expected_cdf(x) for x in plot_x], '-r', label='$F(x)$')
plt.step(rng, rng_cdf, '-k', where='post', label='$F_n(x)$ Numpy')
plt.xlabel('$x$')
plt.ylabel('$P\{X \leq x\}$')
plt.legend(loc='best')

# compute the k-s statistic using a formula
k_values = np.max(np.abs(np.subtract(
        values_cdf, [expected_cdf(x) for x in values])))

# print the results of the scipy.stats k-s test
print stats.kstest(rng, lambda x: x)