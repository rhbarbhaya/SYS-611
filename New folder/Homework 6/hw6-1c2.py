"""
Solution to Homework 6-1c: Cafe Java.

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# import the scipy.stats package and refer to it as `stats`
import scipy.stats as stats

print_output = False
num_runs = 10
W_bar = np.zeros(num_runs)

# define the arrival rate
_lambda = 1./2
# define the service rate
_mu = 2./3
    
# define process generator for x
def generate_x():
    return -np.log(1-np.random.rand())/_lambda

# define process generator for y
def generate_y():
    return -np.log(1-np.random.rand())/_mu

for run in range(num_runs):    
    # initialize random number generator
    np.random.seed(run)
    
    # initialize variables
    t = 0
    t_A = generate_x()
    t_D = np.inf
    N = 0
    N_A = 0
    N_D = 0
    W = 0
    
    if print_output:
        print '{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'.format(
                't', 't_A', 't_D', 'N', 'N_A', 'N_D', 'W')
        print '{:10.2f}{:10.2f}{:10.2f}{:10.0f}{:10.0f}{:10.0f}{:10.2f}'.format(
                t, t_A, t_D, N, N_A, N_D, W)
    
    # loop over each event (customer arrival)
    while t_A < np.inf or t_D < np.inf:
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
                t_D = t + generate_y()
            if t < 600:
                # schedule another arrival
                t_A = t + generate_x()
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
                t_D = t + generate_y()
            else:
                # no one else in the system
                t_D = np.inf
    
        if print_output:
            print '{:10.2f}{:10.2f}{:10.2f}{:10.0f}{:10.0f}{:10.0f}{:10.2f}'.format(
                    t, t_A, t_D, N, N_A, N_D, W)
    if print_output:
        print 'W_bar = {:.2f}'.format(W/N_A)
    # the total wait for customers arriving before time 600
    W_bar[run] = W/N_A
        
print 'Expected W_bar for n={:} runs = {:.2f}'.format(num_runs, np.mean(W_bar))
print '95% C.I. for W_bar for n={:} runs = [{:.2f}, {:.2f}]'.format(
        num_runs, np.mean(W_bar)-1.96*stats.sem(W_bar), np.mean(W_bar)+1.96*stats.sem(W_bar))