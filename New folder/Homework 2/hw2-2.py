# -*- coding: utf-8 -*-
"""
Solution for SYS-611 HW2.2

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

#%% problem 2.2

# seed the random number generator to get consistent results
np.random.seed(0)

# define the values of y using increments of 0.1
y = np.arange(0,20,0.1)

# define the pdf for f(y)
f = 0.02*(y - 5)
# override values < 5 to zero
f[y<5] = 0
# override values > 15 to zero
f[y>15] = 0

# compute the cdf for F(y)
F = 0.01*(y - 5)**2
# override values < 5 to zero
F[y<5] = 0
# override values > 15 to one
F[y>15] = 1

# create a line plot for pdf
plt.figure()
plt.plot(y, f, '-r')
plt.xlabel('y')
plt.ylabel('f(y)')
plt.savefig('hw2-2b.png')

# create a line plot for cdf
plt.figure()
plt.plot(y, F, '-r')
plt.xlabel('y')
plt.ylabel('F(y)')
plt.savefig('hw2-2c.png')

# create a function for a continuous process generator
def gen_sample():
    r = np.random.rand()
    return np.sqrt(r/0.01) + 5

# generate array with 1000 samples
samples = np.array([gen_sample() for i in range(1000)])

# create a histogram of sampled values
plt.figure()
# use automatic bins and set color to red
plt.hist(samples, color='r')
plt.xlabel('y')
plt.ylabel('Frequency')
plt.savefig('hw2-2d.png')

# print out descriptive statistics and confidence interval
print 'y_bar={:.2f}'.format(np.average(samples))
print 's_y={:.2f}'.format(np.std(samples, ddof=1))
print 'SEM={:.3f}'.format(stats.sem(samples))
print '95% CI mu_y=[{:.2f}, {:.2f}]'.format(
        np.average(samples)-stats.norm.ppf(0.975)*stats.sem(samples),
        np.average(samples)+stats.norm.ppf(0.975)*stats.sem(samples))