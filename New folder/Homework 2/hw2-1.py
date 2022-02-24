# -*- coding: utf-8 -*-
"""
Solution for SYS-611 HW2.1

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# import the matplotlib pyplot package and refer to it as `plt`
# see http://matplotlib.org/api/pyplot_api.html for documentation
import matplotlib.pyplot as plt

# import the scipy stats package and refer to it as `stats`
# see http://docs.scipy.org/doc/scipy-0.14.0/reference/stats.html for docs
import scipy.stats as stats

#%% problem 2.1

# seed the random number generator to get consistent results
np.random.seed(0)

# define the values of x
x = np.arange(2,13)

# define the pmf for p(x)
p = np.array([1./36, 2./36, 3./36, 4./36, 5./36, 6./36, 5./36, 4./36, 3./36, 2./36, 1./36])

# print out the p elements, using 2-decimal point formatting, separated by commas
print 'p(x)='+', '.join('{:.2f}'.format(i) for i in p)

# compute the cdf for F(x)
F = np.cumsum(p)

# print out the p elements, using 2-decimal point formatting, separated by commas
print 'F(x)='+', '.join('{:.2f}'.format(i) for i in F)

# create a bar plot for pmf
plt.figure()
plt.bar(x, p, color='r')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.savefig('hw2-1b.png')

# create a line plot for cdf
plt.figure()
plt.step(x, F, '.-r', where='post')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.savefig('hw2-1c.png')

# create a function for a discrete process generator
def gen_sample():
    r = np.random.rand()
    # loop over each index i
    for i in range(len(x)):
        # if the random number is less than the cdf value at this index
        if r <= F[i]:
            # return the corresponding x value for this index
            return x[i]

# generate array with 1000 samples
samples = np.array([gen_sample() for i in range(1000)])

# create a histogram of sampled values
plt.figure()
# use bins boundaries between 2 and 13, scale bars to 80% width, align to left
# side of bins, and set color to red
plt.hist(samples, bins=range(2,14), rwidth=0.8, align='left', color='r')
plt.xlabel('x')
plt.ylabel('Frequency')
plt.savefig('hw2-1d.png')

# print out descriptive statistics and confidence interval
print 'x_bar={:.2f}'.format(np.average(samples))
print 's_x={:.2f}'.format(np.std(samples, ddof=1))
print 'SEM={:.3f}'.format(stats.sem(samples))
print '95% CI mu_x=[{:.2f}, {:.2f}]'.format(
        np.average(samples)-stats.norm.ppf(0.975)*stats.sem(samples),
        np.average(samples)+stats.norm.ppf(0.975)*stats.sem(samples))