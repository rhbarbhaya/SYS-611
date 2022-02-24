"""
Example Discrete Event Simulation for an Inventory Model

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# import the matplotlib pyplot package and refer to it as `plt`
# see http://matplotlib.org/api/pyplot_api.html for documentation
import matplotlib.pyplot as plt
    
def advance_time():
    global t, N_G, P_G, t_G, N_C, P_C, t_C
    
    # generate demand for geophones and converters
    D_G = 0
    D_C = 0
    r = np.random.rand()
    if r < 0.03:
       D_G = 1
       D_C = 2
    elif r < 0.10:
       D_G = 1
       D_C = 3
    elif r < 0.15:
       D_G = 1
       D_C = 5
    elif r < 0.20:
       D_G = 5
       D_C = 2
    elif r < 0.40:
       D_G = 5
       D_C = 3
    elif r < 0.55:
       D_G = 5
       D_C = 5
    elif r < 0.60:
       D_G = 10
       D_C = 2
    elif r < 0.75:
       D_G = 10
       D_C = 3
    else:
       D_G = 10
       D_C = 5
    
    # update the inventory levels based on demands
    N_G -= D_G
    N_C -= D_C
    
    # update penalties according to inventory levels        
    if N_G < 0:
        P_G -= N_G
    if N_C < 0:
        P_C -= N_C
        
    # check if geophones are delivered
    if t_G <= t + 1:
        # set the geophone inventory to 50
        N_G = 50
        # schedule the next geophone delivery in 5 days
        t_G += 5
    
    # check if there should be a new order for converters
    if N_C < 30 and t_C == float('inf'):
        # schedule order by generating lead time
        t_C = t + 5 + np.random.exponential(4)
    
    # check if converters are delivered
    if t_C <= t + 1:
        # add 40 to the converters inventory and reset the delivery time
        N_C += 40
        t_C = float('inf')
    
    # update the simulation time
    t += 1

global t, N_G, P_G, t_G, N_C, P_C, t_C

# initialize clock
t = 0.0

# initialize state
N_G = 50
P_G = 0
t_G = 5
N_C = 40
P_C = 0
t_C = float('inf')

# arrays to record data
obs_time = []
geophone_inventory = []
converter_inventory = []
geophone_penalty = []
converter_penalty = []

# set random number seed
np.random.seed(0)
# iterate over the 260 days
while t < 260.0:
    # advance the simulation
    advance_time()
    # record the simulation state
    obs_time.append(t)
    geophone_inventory.append(N_G)
    converter_inventory.append(N_C)
    geophone_penalty.append(P_G)
    converter_penalty.append(P_C)

# plot the inventory over time
plt.figure()
plt.step(obs_time, geophone_inventory, where='post', label='Geophone')
plt.step(obs_time, converter_inventory, where='post', label='Converter')
plt.xlabel('Time (day)')
plt.ylabel('Inventory Level')
plt.legend(loc='best')
plt.savefig('hw6-2e1.png')

# plot the penalty over time
plt.figure()
plt.step(obs_time, geophone_penalty, where='post', label='Geophone')
plt.step(obs_time, converter_penalty, where='post', label='Converter')
plt.xlabel('Time (day)')
plt.ylabel('Penalty')
plt.legend(loc='best')
plt.savefig('hw6-2e2.png')