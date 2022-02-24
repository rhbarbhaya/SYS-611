"""
Example inventory model in SimPy (object-oriented).

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

class Warehouse(object):
    """ Defines a warehouse simulation. """
    def __init__(self, env, order_cutoff, order_target):
        """ Initializes this warehouse.
        
        Args:
            env (simpy.Environment): the simulation environment
            order_cutoff (int): the cutoff inventory level to place order
            order_target (int): the target inventory level
        """
        self.product_price = 100.00 # dollars per product
        self.product_cost = 50.00 # dollars per product
        self.holding_cost = 2.00 # dollars per product per day
        self.arrival_rate = 5 # customers per day
        self.demand_lb = 1 # products per customer
        self.demand_ub = 4 # products per customer
        self.order_cutoff = order_cutoff # products
        self.order_target = order_target # products
        self.delivery_delay = 2 # days
        
        self.env = env
        self.inventory = order_target
        self.num_ordered = 0
        self.balance = 0
    
    def run(self):
        """ Process to run this simulation. """
        # initialize the customer counter
        i = 0
        # enter infinite loop
        while True:
            # wait for the next arrival
            inter_arrival = np.random.exponential(1./self.arrival_rate)
            yield self.env.timeout(inter_arrival)
            # subtract holding costs
            self.balance -= self.holding_cost*self.inventory*inter_arrival
            # increment a counter
            i += 1
            customer = 'Cust {}'.format(i)
            # generate demand
            demand = np.random.randint(self.demand_lb, self.demand_ub+1) 
            if NUM_RUNS <= 1:
                print '{} demands {} at t={:.2f}'.format(customer, demand, env.now)
            # handle demands
            if self.inventory > demand:
                num_sold = demand
            else:
                num_sold = self.inventory
            self.balance += self.product_price*num_sold
            self.inventory -= num_sold
            if num_sold > 0:
                if NUM_RUNS <= 1:
                    print '{} buys {} at t={:.2f} ({} remaining)'.format(
                            customer, demand, env.now, self.inventory)
            # check for order
            if self.inventory < self.order_cutoff and self.num_ordered == 0:
                quantity = self.order_target - self.inventory
                self.env.process(self.handle_order(quantity))
    
    def handle_order(self, quantity):
        """ Process to place an order.
        
        Args:
            quantity (int): the order quantity
        """
        if NUM_RUNS <= 1:
            print 'order {} at t={}'.format(quantity, env.now)
        self.num_ordered = quantity
        self.balance -= self.product_cost*quantity
        
        # wait for the delivery to arrive
        yield self.env.timeout(self.delivery_delay)
        
        if NUM_RUNS <= 1:
            print 'delivery of {} at t={:.2f}'.format(quantity, env.now)
        self.inventory += quantity
        self.num_ordered = 0

# arrays to record data
queue_wait = []
total_wait = []
obs_time = []
inventory_level = []

def observe(env, warehouse):
    """ Process to observe the warehouse inventory during a simulation.
    
    Args:
        env (simpy.Environment): the simulation environment
        warehouse (Warehouse): the warehouse
    """
    while True:
        # record the observation time and queue length
        obs_time.append(env.now)
        inventory_level.append(warehouse.inventory)
        # wait for the next minute
        yield env.timeout(0.1)

#%% perform coarse analysis with only 10 runs per design option 

s_values = np.linspace(10,120,23)
q_values = np.linspace(10,120,23)

# create a meshgrid of alternatives
order_up_to, order_threshold = np.meshgrid(s_values, q_values, indexing='ij')
# create a matrix of balance values for each alternative
balances = np.zeros((len(s_values), len(q_values)))

NUM_RUNS = 10

# iterate over each alternative
for i_q in range(len(q_values)):
    for i_s in range(len(s_values)):
        if order_up_to[i_s][i_q] < order_threshold[i_s][i_q]:
            balances[i_s][i_q] = 0
        else:
            final_balance = np.zeros(NUM_RUNS)
            # iterate over each run
            for i in range(NUM_RUNS):
                # set the random number seed
                np.random.seed(i)
                
                # create the simpy environment
                env = simpy.Environment()
                # create the warehouse
                warehouse = Warehouse(env, order_threshold[i_s][i_q], order_up_to[i_s][i_q])
                # add the warehouse run process
                env.process(warehouse.run())
                # DO NOT add the observation process -- too slow
                # env.process(observe(env, warehouse))
                # run the simulation for 100 days
                env.run(until=100)
                
                final_balance[i] = warehouse.balance
            # compute the average cost over all the runs
            balances[i_s][i_q] = np.mean(final_balance)

# create a contour plot based on the computed data with 20 levels
plt.figure()
cs = plt.contour(order_up_to, order_threshold, balances, 20)
plt.xlabel('Order Up To (S)')
plt.ylabel('Order Threshold (Q)')
plt.clabel(cs)

plt.savefig('hw7-1a.png')

#%% perform fine analysis

s_values = np.linspace(65,75,11)
q_values = np.linspace(35,45,11)

# create a meshgrid of alternatives
order_up_to, order_threshold = np.meshgrid(s_values, q_values, indexing='ij')
# create a matrix of balance values for each alternative
balances = np.zeros((len(s_values), len(q_values)))

NUM_RUNS = 100

# iterate over each alternative
for i_q in range(len(q_values)):
    for i_s in range(len(s_values)):
        if order_up_to[i_s][i_q] < order_threshold[i_s][i_q]:
            balances[i_s][i_q] = 0
        else:
            final_balance = np.zeros(NUM_RUNS)
            # iterate over each run
            for i in range(NUM_RUNS):
                # set the random number seed
                np.random.seed(i)
                
                # create the simpy environment
                env = simpy.Environment()
                # create the warehouse
                warehouse = Warehouse(env, order_threshold[i_s][i_q], order_up_to[i_s][i_q])
                # add the warehouse run process
                env.process(warehouse.run())
                # DO NOT add the observation process -- too slow
                # env.process(observe(env, warehouse))
                # run the simulation for 100 days
                env.run(until=100)
                
                final_balance[i] = warehouse.balance
            # compute the average cost over all the runs
            balances[i_s][i_q] = np.mean(final_balance)

# create a contour plot based on the computed data with 20 levels
plt.figure()
cs = plt.contour(order_up_to, order_threshold, balances, 20)
plt.xlabel('Order Up To (S)')
plt.ylabel('Order Threshold (Q)')
plt.clabel(cs)

plt.savefig('hw7-1b.png')

#%% perform final analysis

NUM_RUNS = 1000

final_balance_1 = np.zeros(NUM_RUNS)
final_balance_2 = np.zeros(NUM_RUNS)

for i in range(NUM_RUNS):
    # set the random number seed
    np.random.seed(i)
    
    # create the simpy environment
    env = simpy.Environment()
    # create the warehouse
    warehouse = Warehouse(env, 37, 68)
    # add the warehouse run process
    env.process(warehouse.run())
    # DO NOT add the observation process -- too slow
    # env.process(observe(env, warehouse))
    # run the simulation for 100 days
    env.run(until=100)
    # record result
    final_balance_1[i] = warehouse.balance

for i in range(NUM_RUNS):
    # set the random number seed
    np.random.seed(i)
    
    # create the simpy environment
    env = simpy.Environment()
    # create the warehouse
    warehouse = Warehouse(env, 38, 69)
    # add the warehouse run process
    env.process(warehouse.run())
    # DO NOT add the observation process -- too slow
    # env.process(observe(env, warehouse))
    # run the simulation for 100 days
    env.run(until=100)
    # record result
    final_balance_2[i] = warehouse.balance

# import the scipy stats package and refer to it as `stats`
# see https://docs.scipy.org/doc/scipy/reference/stats.html for documentation
import scipy.stats as stats

z_crit = stats.norm.ppf(0.975)

print 'Mean cost with Q=38, S=69: {:.2f} +- {:.2f}'.format(
    np.mean(final_balance_1), stats.sem(final_balance_1*z_crit))

print 'Mean cost with Q=38, S=69: {:.2f} +- {:.2f}'.format(
    np.mean(final_balance_2), stats.sem(final_balance_2)*z_crit)