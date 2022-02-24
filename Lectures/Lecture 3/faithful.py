"""
Example: Visualizing the Old Faithful data set.

This example creates a scatter plot of eruption time versus waiting time until
the next eruption for a set of 272 observations.

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
# see https://docs.scipy.org/doc/scipy/reference/ for documentation
import scipy.stats as stats

# read the  csv file into a data frame
df = pd.read_csv('faithful.csv')

# create a new plot figure
plt.figure()
# plot eruptions vs. waiting using a blue dot (.b) format
plt.plot(df['eruptions'], df['waiting'], '.b', label='Observations')
# label the x- and y-axes
plt.xlabel('Eruption Duration')
plt.ylabel('Waiting Time')
# add a legend in the 'best' location
plt.legend(loc='best')

# compute and print the mean and standard deviation for eruptions
duration_mean = np.mean(df['eruptions'])
print "Eruption Duration Mean: {:.2f} minutes".format(duration_mean)
duration_std = np.std(df['eruptions'], ddof=1)
print "Eruption Duration St. Dev.: {:.2f} minutes".format(duration_std)

# compute and print the mean and standard deviation for waiting
wait_mean = np.mean(df['waiting'])
print "Time between Eruptions Mean: {:.2f} minutes".format(wait_mean)
wait_std = np.std(df['waiting'], ddof=1)
print "Time between Eruptions St. Dev.: {:.2f} minutes".format(wait_std)

# plot the standard deviations with red color (r)
plt.errorbar(duration_mean, wait_mean, fmt='xr',
             xerr=duration_std, yerr=wait_std, 
             label='Descriptive Statistics')
             
# add a legend in the 'best' location
plt.legend(loc='best')

# perform the polynomial regression using the eruptions 
# and waiting for 1st order (y = m*x + b)
coefs = np.polyfit(df['eruptions'], df['waiting'], 1)

# print the regression equation formatted in floating-point with 2 decimals
print "y_2 = {:.2f}x + {:.2f}".format(coefs[0], coefs[1])

# create a numpy array with the points [1.5, 5.5]
regression_x = np.array([1.5, 5.5])
# compute the regression y-values using numpy vector math functions
# note: this function is *not* supported by default python lists
regression_y = coefs[0]*regression_x + coefs[1]

# plot the regression with a dotted red line (:r)
plt.plot(regression_x, regression_y, ':r', label='Linear Regression')

# add a legend in the 'best' location
plt.legend(loc='best')

# compute the correlation coefficient
r, p = stats.pearsonr(df['eruptions'], df['waiting'])
# print the r-squared value
print "r^2 value: {:.2f}".format(r**2)