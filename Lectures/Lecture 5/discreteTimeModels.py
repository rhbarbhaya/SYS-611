"""
SYS-611 Discrete Time Models.

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the matplotlib pyplot package and refer to it as `plt`
# see http://matplotlib.org/api/pyplot_api.html for documentation
import matplotlib.pyplot as plt

#%% delay system example

# define the input trajectory
x = [1,1,0,0,1,0,0,0,1]

# define the state update function
def _delta(q, x): 
    return x
    
# define the output function
def _lambda(q, x): 
    return x
    
# define the output and state trajectories
y = [0,0,0,0,0,0,0,0,0]
q = [0,0,0,0,0,0,0,0,0,0]

# initialize the simulation
t = 0
q[0] = 0

# execute the simulation
while t <= 8:
    # record output value
    y[t] = _lambda(q[t], x[t])
    # record state update
    q[t+1] = _delta(q[t], x[t])
    # advance time
    t += 1

plt.figure()
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
ax1.bar(range(9), x, color='k')
ax1.set_ylabel('Input ($x$)')
ax2.bar(range(9), q[:-1], color='k')
ax2.set_ylabel('State ($q$)')
ax3.bar(range(9), y, color='k')
ax3.set_ylabel('Output ($y$)')
plt.xlabel('Time (ticks)')
plt.suptitle('Delay System Model')

#%% binary counter example

# define the input trajectory
x = [1,1,0,0,1,0,0,0,1]

# define the state update function
def _delta(q, x): 
    return q != x
    
# define the output function
def _lambda(q, x): 
    return q and x
    
# define the output and state trajectories
y = [0,0,0,0,0,0,0,0,0]
q = [0,0,0,0,0,0,0,0,0,0]

# initialize the simulation
t = 0
q[0] = 0

# execute the simulation
while t <= 8:
    # record output value
    y[t] = _lambda(q[t], x[t])
    # record state update
    q[t+1] = _delta(q[t], x[t])
    # advance time
    t += 1

plt.figure()
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
ax1.bar(range(9), x, color='k')
ax1.set_ylabel('Input ($x$)')
ax2.bar(range(9), q[:-1], color='k')
ax2.set_ylabel('State ($q$)')
ax3.bar(range(9), y, color='k')
ax3.set_ylabel('Output ($y$)')
plt.xlabel('Time (ticks)')
plt.suptitle('Binary Counter Model')

#%% delay flip-flop example

# define the input trajectory
x = [1,1,0,0,1,0,0,0,1]

# define the state update function
def _delta(q, x): 
    return x
    
# define the output function
def _lambda(q): 
    return q
    
# define the output and state trajectories
y = [0,0,0,0,0,0,0,0,0]
q = [0,0,0,0,0,0,0,0,0,0]

# initialize the simulation
t = 0
q[0] = 0

# execute the simulation
while t <= 8:
    # record output value
    y[t] = _lambda(q[t])
    # record state update
    q[t+1] = _delta(q[t], x[t])
    # advance time
    t += 1

plt.figure()
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
ax1.bar(range(9), x, color='k')
ax1.set_ylabel('Input ($x$)')
ax2.bar(range(9), q[:-1], color='k')
ax2.set_ylabel('State ($q$)')
ax3.bar(range(9), y, color='k')
ax3.set_ylabel('Output ($y$)')
plt.xlabel('Time (ticks)')
plt.suptitle('Delay Flip-Flop Model')

#%% linear moore network example

# define the state update function
def _delta(q, x): 
    return x
    
# define the output function
def _lambda(q): 
    return q
    
# define the state trajectories
q_1 = [0,0,0,0,0,0,0,0,0,0]
q_2 = [0,0,0,0,0,0,0,0,0,0]

# initialize the simulation
t = 0
q_1[0] = 1
q_2[0] = 1

# define the gain
gain = 0.8

# execute the simulation
while t <= 8:
    # record state update
    q_1[t+1] = _delta(q_1[t], -gain*_lambda(q_2[t]))
    q_2[t+1] = _delta(q_2[t], gain*_lambda(q_1[t]))
    # advance time
    t += 1

plt.figure()
f, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(range(9), q_1[:-1], 'or')
ax1.set_ylabel('State ($q_1$)')
ax1.set_ylim([-1.2,1.2])
ax2.plot(range(9), q_2[:-1], 'ob')
ax2.set_ylabel('State ($q_2$)')
ax2.set_ylim([-1.2,1.2])
plt.xlabel('Time (ticks)')
plt.suptitle('Linear Moore Network Model ($g=0.8$)')