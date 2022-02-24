"""
Solution to Homework 6-1a: Cafe Java.

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# generate the inter-arrival and service times uing the IVT method
x = [0.42, 1.53, 0.12, 0.84, 0.16]
y = [1.68, 0.78, 0.06, 0.02, 2.01]

# define the number of events and create arrays to store results
num_events = 5
t_enter = np.zeros(num_events)
q_length = np.zeros(num_events)
t_served = np.zeros(num_events)
q_wait = np.zeros(num_events)
t_exit = np.zeros(num_events)
total_wait = np.zeros(num_events)

print '{:>4s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'.format(
        'i', 'x_i', 't_enter', 'L_q', 't_served', 'W_q', 'y_i', 't_exit', 'W')

# loop over each event (customer arrival)
for i in range(num_events):
    # entry time is appended to the previous entry time
    # or equal to arrival time for first customer
    t_enter[i] = t_enter[i-1] + x[i] if i > 0 else x[i]
    # queue length is the number of customers who have not yet exited
    # or zero for the first customer
    q_length[i] = np.sum(t_exit[0:i] > t_enter[i]) if i > 0 else 0
    # time served is the exit time of previous customer if in queue
    # or entry time if no queue
    t_served[i] = np.max(t_exit[i-1]) if q_length[i] > 0 else t_enter[i]
    # waiting time in queue is service time minus entry time
    q_wait[i] = t_served[i]-t_enter[i]
    # exit time is time served plus service time
    t_exit[i] = t_served[i] + y[i]
    # total wait is exit time minus entry time
    total_wait[i] = t_exit[i] - t_enter[i]
    
    # print results
    print '{:4d}{:10.2f}{:10.2f}{:10.0f}{:10.2f}{:10.2f}{:10.2f}{:10.2f}{:10.2f}'.format(
            i+1, x[i], t_enter[i], q_length[i], t_served[i], 
            q_wait[i], y[i], t_exit[i], total_wait[i])