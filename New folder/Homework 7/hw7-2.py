"""
Solution to SYS-611 HW 7-2: Factory Simulation Analysis

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the simpy package 
# see https://simpy.readthedocs.io/en/latest/api_reference for documentation
import simpy

# import the numpy package and refer to it as `np`
# see http://docs.scipy.org/doc/numpy/reference/ for documentation
import numpy as np

# import the matplotlib pyplot package and refer to it as `plt`
# see http://matplotlib.org/api/pyplot_api.html for documentation
import matplotlib.pyplot as plt

class Factory(object):
    """ Defines a factory simulation. """
    def __init__(self, env, num_repairers, num_spares):
        """ Initializes this factory.
        
        Args:
            env (simpy.Environment): the simulation environment
            num_repairers (int): the number of repairers to hire
            num_spares (int): the number of spares to purchase
        """
        self.repairers = simpy.Resource(env, capacity=num_repairers) 
        self.spares = simpy.Container(env, init=num_spares, capacity=num_spares)
        self.env = env
        self.cost = 0
        self.daily_cost = 3.75*8*num_repairers + 30*num_spares
    
    def run(self):
        """ Process to run this simulation. """
        # launch the 50 machine processes
        for i in range(50):
            self.env.process(factory.operate_machine(i+1))
        # update the daily costs each day
        while True:
            self.cost += self.daily_cost
            yield self.env.timeout(8.0)
    
    def operate_machine(self, machine):
        """ Process to operate a machine.
        
        Args:
            machine (int): the machine number
        """
        while True:
            # wait until the machine breaks
            yield self.env.timeout(np.random.uniform(132,182))
            time_broken = self.env.now
            #print 'machine {} broke at {:.2f} ({} spares available)'.format(
            #        machine, time_broken, self.spares.level)
            # launch the repair process
            self.env.process(self.repair_machine())
            # wait for a spare to become available
            yield self.spares.get(1)
            time_replaced = self.env.now
            #print 'machine {} replaced at {:.2f}'.format(machine, time_replaced)
            # update the cost for being out of service
            self.cost += 20*(time_replaced-time_broken)
              
    def repair_machine(self):
        """ Process to repair a machine. """
        with self.repairers.request() as request:
            # wait for a repairer to become available
            yield request
            # perform the repair
            yield self.env.timeout(np.random.uniform(4,10))
            # put the machine back in the spares pool
            yield self.spares.put(1)
            #print 'repair complete at {:.2f} ({} spares available)'.format(
            #        self.env.now, self.spares.level)

# arrays to record data
obs_time = []
obs_cost = []
obs_spares = []

def observe(env, factory):
    """ Process to observe the factory during a simulation.
    
    Args:
        env (simpy.Environment): the simulation environment
        factory (Factory): the factory
    """
    while True:
        obs_time.append(env.now)
        obs_cost.append(factory.cost)
        obs_spares.append(factory.spares.level)
        yield env.timeout(1.0)

#%% perform coarse analysis with only 5 runs per design option 

MIN_SPARES = 1
MAX_SPARES = 10
MIN_REPAIRERS = 2
MAX_REPAIRERS = 10
# create a meshgrid of alternatives
repairers, spares = np.meshgrid(np.arange(MIN_REPAIRERS, MAX_REPAIRERS + 1), 
                                np.arange(MIN_SPARES, MAX_SPARES + 1), indexing='ij')
# create a matrix of cost values for each alternative
costs = np.zeros((MAX_REPAIRERS - MIN_REPAIRERS + 1, MAX_SPARES - MIN_SPARES + 1))

NUM_RUNS = 5

# iterate over each alternative
for i_r in range(MAX_REPAIRERS - MIN_REPAIRERS + 1):
    for i_s in range(MAX_SPARES - MIN_SPARES + 1):
        final_cost = np.zeros(NUM_RUNS)
        
        # iterate over each run
        for i in range(NUM_RUNS):
            # set the random number seed
            np.random.seed(i)
            
            # create the simpy environment
            env = simpy.Environment()
            # create the factory
            factory = Factory(env, repairers[i_r][i_s], spares[i_r][i_s])
            # add the factory run process
            env.process(factory.run())
            # DO NOT add the observation process -- too slow
            # env.process(observe(env, factory))
            # run simulation for one year
            env.run(until=8*5*52)
            
            final_cost[i] = factory.cost
        # compute the average cost over all the runs
        costs[i_r][i_s] = np.mean(final_cost)

# create a contour plot based on the computed data with 20 levels
plt.figure()
cs = plt.contour(repairers, spares, costs, 20)
plt.xlabel('Number Repairers')
plt.ylabel('Number Spares')
plt.clabel(cs)

plt.savefig('hw7-2a.png')

#%% perform fine analysis

MIN_SPARES = 3
MAX_SPARES = 5
MIN_REPAIRERS = 3
MAX_REPAIRERS = 6
# create a meshgrid of alternatives
repairers, spares = np.meshgrid(np.arange(MIN_REPAIRERS, MAX_REPAIRERS + 1), 
                                np.arange(MIN_SPARES, MAX_SPARES + 1), indexing='ij')
# create a matrix of cost values for each alternative
costs = np.zeros((MAX_REPAIRERS - MIN_REPAIRERS + 1, MAX_SPARES - MIN_SPARES + 1))

NUM_RUNS = 50

# iterate over each alternative
for i_r in range(MAX_REPAIRERS - MIN_REPAIRERS + 1):
    for i_s in range(MAX_SPARES - MIN_SPARES + 1):
        final_cost = np.zeros(NUM_RUNS)
        
        # iterate over each run
        for i in range(NUM_RUNS):
            # set the random number seed
            np.random.seed(i)
            
            # create the simpy environment
            env = simpy.Environment()
            # create the factory
            factory = Factory(env, repairers[i_r][i_s], spares[i_r][i_s])
            # add the factory run process
            env.process(factory.run())
            # DO NOT add the observation process -- too slow
            # env.process(observe(env, factory))
            # run simulation for one year
            env.run(until=8*5*52)
            
            final_cost[i] = factory.cost
        # compute the average cost over all the runs
        costs[i_r][i_s] = np.mean(final_cost)

# create a contour plot based on the computed data with 20 levels
plt.figure()
cs = plt.contour(repairers, spares, costs, 20)
plt.xlabel('Number Repairers')
plt.ylabel('Number Spares')
plt.clabel(cs)

plt.savefig('hw7-2b.png')

#%% perform final analysis

NUM_RUNS = 1000

final_cost_1 = np.zeros(NUM_RUNS) # 4 repairers, 4 spares
final_cost_2 = np.zeros(NUM_RUNS) # 5 repairers, 4 spares

for i in range(NUM_RUNS):
    # set the random number seed
    np.random.seed(i)
    
    # create the simpy environment
    env = simpy.Environment()
    # create the factory
    factory = Factory(env, 4, 4)
    # add the factory run process
    env.process(factory.run())
    # DO NOT add the observation process -- too slow
    # env.process(observe(env, factory))
    # run simulation for one year
    env.run(until=8*5*52)
    final_cost_1[i] = factory.cost
    
for i in range(NUM_RUNS):
    # set the random number seed
    np.random.seed(i)
    
    # create the simpy environment
    env = simpy.Environment()
    # create the factory
    factory = Factory(env, 5, 4)
    # add the factory run process
    env.process(factory.run())
    # DO NOT add the observation process -- too slow
    # env.process(observe(env, factory))
    # run simulation for one year
    env.run(until=8*5*52)
    
    final_cost_2[i] = factory.cost

    
# import the scipy stats package and refer to it as `stats`
# see https://docs.scipy.org/doc/scipy/reference/stats.html for documentation
import scipy.stats as stats

z_crit = stats.norm.ppf(0.975)

print 'Mean cost with 4 repairers, 4 spares: {:.2f} +- {:.2f}'.format(
    np.mean(final_cost_1), stats.sem(final_cost_1)*z_crit)

print 'Mean cost with 5 repairers, 4 spares: {:.2f} +- {:.2f}'.format(
    np.mean(final_cost_2), stats.sem(final_cost_2)*z_crit)
