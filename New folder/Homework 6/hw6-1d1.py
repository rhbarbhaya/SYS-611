"""
Solution to Homework 6-1d: Cafe Java.

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
    
# define process generator for x
def generate_x(t):
    if t <180:
        _lambda = 0.5
    elif t < 420:
        _lambda = 1.0
    else:
        _lambda = 0.25
    return -np.log(1-np.random.rand())/_lambda

# define process generator for y
def generate_y():
    if np.random.rand() < 0.7:
        _mu = 4./3
    else:
        _mu = 0.5
    return -np.log(1-np.random.rand())/_mu

for run in range(num_runs):
    # initialize random number generator
    np.random.seed(run)
    
    # define the number of events and create arrays to store results
    num_events = 400
    t_enter = np.zeros(num_events)
    q_length = np.zeros(num_events)
    t_served = np.zeros(num_events)
    q_wait = np.zeros(num_events)
    t_exit = np.zeros(num_events)
    total_wait = np.zeros(num_events)
    
    # loop over each event (customer arrival)
    for i in range(num_events):
        # entry time is appended to the previous entry time
        # or equal to arrival time for first customer
        t_enter[i] = t_enter[i-1] + generate_x(t_enter[i-1]) if i > 0 else generate_x(0)
        # queue length is the number of customers who have not yet exited
        # or zero for the first customer
        q_length[i] = np.sum(t_exit[0:i] > t_enter[i]) if i > 0 else 0
        # time served is the exit time of previous customer if in queue
        # or entry time if no queue
        t_served[i] = np.max(t_exit[i-1]) if q_length[i] > 0 else t_enter[i]
        # waiting time in queue is service time minus entry time
        q_wait[i] = t_served[i]-t_enter[i]
        # exit time is time served plus service time
        t_exit[i] = t_served[i] + generate_y()
        # total wait is exit time minus entry time
        total_wait[i] = t_exit[i] - t_enter[i]
    
    # print out the results
    if print_output:
        print '{:>4s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'.format(
                'i', 't_enter', 'L_q', 't_served', 'W_q', 't_exit', 'W')
        for i in range(sum(t_enter<600)):
            print '{:4d}{:10.2f}{:10.0f}{:10.2f}{:10.2f}{:10.2f}{:10.2f}'.format(
                    i, t_enter[i], q_length[i], t_served[i], 
                    q_wait[i], t_exit[i], total_wait[i])
    
        print 'W_bar = {:.2f}'.format(np.mean(total_wait[t_enter<600]))
    # the total wait for customers arriving before time 600
    W_bar[run] = np.mean(total_wait[t_enter<600])

print 'Expected W_bar for n={:} runs = {:.2f}'.format(num_runs, np.mean(W_bar))
print '95% C.I. for W_bar for n={:} runs = [{:.2f}, {:.2f}]'.format(
        num_runs, np.mean(W_bar)-1.96*stats.sem(W_bar), np.mean(W_bar)+1.96*stats.sem(W_bar))
