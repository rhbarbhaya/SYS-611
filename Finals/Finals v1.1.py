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

# Team B Person 1
NCBP_B1 = True # Car being produced by person 1 from Team B
Time_Start_B1 = [0] # Starting time for B1
Time_End_B1 = [] # Ending time for B1
Person_ID_B1 = [] # Team A person ID
Time_Taken_B1 = []
Cost_B1 = []
Profit_B1 = []
Revenue_B1 = []
# Team B Person 2
NCBP_B2 = True # Car being produced by person 2 from Team B
Time_Start_B2 = [0] # Starting time for B2
Time_End_B2 = [] # Ending time for B2
Person_ID_B2 = [] # Team A person ID
Time_Taken_B2 = []
Cost_B2 = []
Profit_B2 = []
Revenue_B2 = []
# Team B Person 3
NCBP_B3 = True # Car being produced by person 3 from Team B
Time_Start_B3 = [0] # Starting time for B3
Time_End_B3 = [] # Ending time for B3
Person_ID_B3 = [] # Team A person ID
Time_Taken_B3 = []
Cost_B3 = []
Profit_B3 = []
Revenue_B3 = []
# Team B Person 4
NCBP_B4 = True # Car being produced by person 4 from Team B
Time_Start_B4 = [0] # Starting time for B4
Time_End_B4 = [] # Ending time for B4
Person_ID_B4 = [] # Team A person ID
Time_Taken_B4 = []
Cost_B4 = []
Profit_B4 = []
Revenue_B4 = []

def B1(env):
    global NCBP_B1
    while True:
        if NCBP_B1 == True:
            NCBP_B1 = False
            Duration_B1 = np.random.uniform(40.0, 60.0)
            Time_Taken_B1.append(Duration_B1)
            Time_End = Time_Taken_B1[-1] + Time_Start_B1[-1]
            Time_End_B1.append(Time_End)
            Cost_B1.append(Cost)
            Person_ID_B1.append("B-1")
            yield env.timeout(Duration_B1)
        elif NCBP_B1 == False and env.now == Time_End_B1[-1]:
            Revenue_B1.append(Revenue)
            Profit_B1.append(Profit)
            Time_Start_B1.append(Time_End_B1[-1])
            NCBP_B1 = True
            yield env.timeout(0)

def B2(env):
    global NCBP_B2
    while True:
        if NCBP_B2 == True:
            NCBP_B2 = False
            Duration_B2 = np.random.uniform(40.0, 60.0)
            Time_Taken_B2.append(Duration_B2)
            Time_End = Time_Taken_B2[-1] + Time_Start_B2[-1]
            Time_End_B2.append(Time_End)
            Cost_B2.append(Cost)
            Person_ID_B2.append("B-2")
            yield env.timeout(Duration_B2)
        elif NCBP_B2 == False and env.now == Time_End_B2[-1]:
            Revenue_B2.append(Revenue)
            Profit_B2.append(Profit)
            Time_Start_B2.append(Time_End_B2[-1])
            NCBP_B2 = True
            yield env.timeout(0)

def B3(env):
    global NCBP_B3
    while True:
        if NCBP_B3 == True:
            NCBP_B3 = False
            Duration_B3 = np.random.uniform(40.0, 60.0)
            Time_Taken_B3.append(Duration_B3)
            Time_End = Time_Taken_B3[-1] + Time_Start_B3[-1]
            Time_End_B3.append(Time_End)
            Cost_B3.append(Cost)
            Person_ID_B3.append("B-3")
            yield env.timeout(Duration_B3)
        elif NCBP_B3 == False and env.now == Time_End_B3[-1]:
            Revenue_B3.append(Revenue)
            Profit_B3.append(Profit)
            Time_Start_B3.append(Time_End_B3[-1])
            NCBP_B3 = True
            yield env.timeout(0)

def B4(env):
    global NCBP_B4
    while True:
        if NCBP_B4 == True:
            NCBP_B4 = False
            Duration_B4 = np.random.uniform(40.0, 60.0)
            Time_Taken_B4.append(Duration_B4)
            Time_End = Time_Taken_B4[-1] + Time_Start_B4[-1]
            Time_End_B4.append(Time_End)
            Cost_B4.append(Cost)
            Person_ID_B4.append("B-4")
            yield env.timeout(Duration_B4)
        elif NCBP_B4 == False and env.now == Time_End_B4[-1]:
            Revenue_B4.append(Revenue)
            Profit_B4.append(Profit)
            Time_Start_B4.append(Time_End_B4[-1])
            NCBP_B4 = True
            yield env.timeout(0)

env = simpy.Environment()
env.process(B1(env))
env.process(B2(env))
env.process(B3(env))
env.process(B4(env))
env.run(until = Time_Limit)
B1 = pd.DataFrame([Time_Start_B1, Person_ID_B1, Cost_B1, Revenue_B1, Profit_B1, Time_Taken_B1, Time_End_B1]).transpose()
B1.columns = ("Start Time", "Person_ID", "Cost", "Revenue", "Profit", "Time Taken", "Time End")
B2 = pd.DataFrame([Time_Start_B2, Person_ID_B2, Cost_B2, Revenue_B2, Profit_B2, Time_Taken_B2, Time_End_B2]).transpose()
B2.columns = ("Start Time", "Person_ID", "Cost", "Revenue", "Profit", "Time Taken", "Time End")
B3 = pd.DataFrame([Time_Start_B3, Person_ID_B3, Cost_B3, Revenue_B3, Profit_B3, Time_Taken_B3, Time_End_B3]).transpose()
B3.columns = ("Start Time", "Person_ID", "Cost", "Revenue", "Profit", "Time Taken", "Time End")
B4 = pd.DataFrame([Time_Start_B4, Person_ID_B4, Cost_B4, Revenue_B4, Profit_B4, Time_Taken_B4, Time_End_B4]).transpose()
B4.columns = ("Start Time", "Person_ID", "Cost", "Revenue", "Profit", "Time Taken", "Time End")