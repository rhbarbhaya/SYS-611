"""
Solution to Homework 6-1b: Cafe Java.

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# generate the inter-arrival and service times uing the IVT method
x = [0.42, 1.53, 0.12, 0.84, 0.16]
y = [1.68, 0.78, 0.06, 0.02, 2.01]

# define the number of events
num_events = 10

print '{:>4s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'.format(
        'i', 't', 't_A', 't_D', 'N', 'N_A', 'N_D', 'W')

# initialize variables
t = 0
t_A = x[0]
t_D = np.inf
N = 0
N_A = 0
N_D = 0
W = 0

print '{:4d}{:10.2f}{:10.2f}{:10.2f}{:10.0f}{:10.0f}{:10.0f}{:10.2f}'.format(
        0, t, t_A, t_D, N, N_A, N_D, W)

# loop over each event (customer arrival)
for i in range(num_events):
    # determine the next event
    t_e = min(t_A,t_D)
    # update the total waiting time
    W += N*(t_e-t)
    # update the simulation time
    t = t_e
    
    if t_A <= t_D:
        # this is an arrival - increment the state variable
        N += 1
        # record an arrival
        N_A += 1
        if N <= 1:
            # schedule the departure
            t_D = t + y[N_D]
        if N_A < 5:
            # schedule another arrival
            t_A = t + x[N_A]
        else:
            # no more customers to schedule
            t_A = np.inf
    else:
        # this is a departure - decrement the state variable
        N -= 1
        # record a departure
        N_D += 1
        if N > 0:
            # schedule the next departure
            t_D = t + y[N_D]
        else:
            # no one else in the system
            t_D = np.inf

    print '{:4d}{:10.2f}{:10.2f}{:10.2f}{:10.0f}{:10.0f}{:10.0f}{:10.2f}'.format(
            i, t, t_A, t_D, N, N_A, N_D, W)