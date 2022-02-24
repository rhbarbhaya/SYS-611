# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:06:52 2018

@author: Alkim & Rushabh
"""
import numpy as np
import simpy
import pandas as pd

Cost = 30 # Price in $
Revenue = 105 # Price in $
Profit = Revenue - Cost # Profit will remain the same so decaring that variable
Time_Limit = 1000 # Time of experiment
NCBP_A1 = True # Car being produced by person 1 from Team A
Time_Start_A1 = [0] # Starting time for A1
Time_End_A1 = [] # Ending time for A1
Indv_A1 = "A-1" # Team A person ID
Time_Taken_A1 = []
Cost_A1 = []
Profit_A1 = []
Revenue_A1 = []

def A1(env):
    global NCBP_A1
    while True:
        if NCBP_A1 == True:
            NCBP_A1 = False
            Rand_A1 = np.random.uniform(10.0, 20.0)
            Time_End_A1.append(Rand_A1)
            Cost_A1.append(Cost)
            yield env.timeout(Rand_A1)
        elif NCBP_A1 == False and env.now == sum(Time_End_A1):
			Revenue_A1.append(Revenue)
			Profit_A1.append(Profit)
			time_taken = Time_End_A1[-1] - Time_Start_A1[-1]
			Time_Taken_A1.append(time_taken)
			Time_Start_A1.append(sum(Time_End_A1))
			NCBP_A1 = True
			yield env.timeout(0)

env = simpy.Environment()
env.process(A1(env))
env.run(until = 1000)
A1 = pd.DataFrame([Time_Start_A1, Cost_A1, Revenue_A1, Profit_A1, Time_Taken_A1]).transpose()
A1.columns = ("Start Time", "Cost", "Revenue", "Profit", "Time Taken")