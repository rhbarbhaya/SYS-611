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

# Team Limits
Team_A_Low_1 = 10.0
Team_A_High_1 = 12.0
Team_A_Low_2 = 8.0
Team_A_High_2 = 10.0
Team_A_Low_3 = 5.0
Team_A_High_3 = 6.0
Team_A_Low_4 = 3.0
Team_A_High_4 = 5.0
Team_B_Low = 60.0
Team_B_High = 80.0

# Team A - 4 person team
NCBP_A1 = True
NCBP_A2 = True
NCBP_A3 = True
NCBP_A4 = True
Time_Start_A1 = [0]
Time_Start_A2 = []
Time_Start_A3 = []
Time_Start_A4 = []
Time_End_A1 = []
Time_End_A2 = []
Time_End_A3 = []
Time_End_A4 = []
Time_Taken_A1 =[]
Time_Taken_A2 =[]
Time_Taken_A3 =[]
Time_Taken_A4 =[]
counterAB = 0
counterBC = 0
counterCD = 0
Cost_A = []
Revenue_A = []
Profit_A = []
Team_ID_A = []
Person_ID_A = []

# Team B Person 1
NCBP_B1 = True # Car being produced by person 1 from Team B
Time_Start_B1 = [0] # Starting time for B1
Time_End_B1 = [] # Ending time for B1
Person_ID_B1 = [] # Team A person ID
Team_ID_B1 = []
Time_Taken_B1 = []
Cost_B1 = []
Profit_B1 = []
Revenue_B1 = []
# Team B Person 2
NCBP_B2 = True # Car being produced by person 2 from Team B
Time_Start_B2 = [0] # Starting time for B2
Time_End_B2 = [] # Ending time for B2
Team_ID_B2 = []
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
Team_ID_B3 = []
Time_Taken_B3 = []
Cost_B3 = []
Profit_B3 = []
Revenue_B3 = []
# Team B Person 4
NCBP_B4 = True # Car being produced by person 4 from Team B
Time_Start_B4 = [0] # Starting time for B4
Time_End_B4 = [] # Ending time for B4
Person_ID_B4 = [] # Team A person ID
Team_ID_B4 = []
Time_Taken_B4 = []
Cost_B4 = []
Profit_B4 = []
Revenue_B4 = []

def A(env, people_a1, people_a2, people_a3, people_a4):
    global counterAB, counterBC, counterCD
    while True:
       with people_a1.request() as req:
           yield req
           Duration_A1 = np.random.uniform(Team_A_Low_1, Team_A_High_1)
           Time_Taken_A1.append(Duration_A1)
           time_end_a1 = Time_Start_A1[-1] + Time_Taken_A1[-1]
           Time_End_A1.append(time_end_a1)
           Cost_A.append(Cost)
           Time_Start_A1.append(Time_End_A1[-1])
           Time_Start_A2.append(Time_End_A1[-1])
           counterAB += 1
           yield env.timeout(Duration_A1)
           people_a1.release(req)
       if counterAB > 0:
           with people_a2.request() as req2:
               yield req2
               counterAB -= 1
               Duration_A2 = np.random.uniform(Team_A_Low_2, Team_A_High_2)
               Time_Taken_A2.append(Duration_A2)
               time_end_a2 = Time_Start_A2[-1] + Time_Taken_A2[-1]
               Time_End_A2.append(time_end_a2)
               Time_Start_A3.append(Time_End_A2[-1])
               counterBC += 1
               yield env.timeout(Duration_A2)
               people_a2.release(req2)
       if counterBC > 0:
           with people_a3.request() as req3:
               yield req3
               counterBC -= 1
               Duration_A3 = np.random.uniform(Team_A_Low_3, Team_A_High_3)
               Time_Taken_A3.append(Duration_A3)
               time_end_a3 = Time_Start_A3[-1] + Time_Taken_A3[-1]
               Time_End_A3.append(time_end_a3)
               Time_Start_A4.append(Time_End_A3[-1])
               counterCD += 1
               yield env.timeout(Duration_A3)
               people_a3.release(req3)
       if counterCD > 0:
           with people_a4.request() as req4:
               yield req4
               counterCD -= 1
               Duration_A4 = np.random.uniform(Team_A_Low_4, Team_A_High_4)
               Time_Taken_A4.append(Duration_A4)
               time_end_a4 = Time_Start_A4[-1] + Time_Taken_A4[-1]
               Time_End_A4.append(time_end_a4)
               Revenue_A.append(Revenue)
               Profit_A.append(Profit)
               yield env.timeout(Duration_A4)
               people_a4.release(req4)

def B1(env):
    global NCBP_B1
    while True:
        if NCBP_B1 == True:
            NCBP_B1 = False
            Duration_B1 = np.random.uniform(Team_B_Low, Team_B_High)
            Time_Taken_B1.append(Duration_B1)
            Time_End = Time_Taken_B1[-1] + Time_Start_B1[-1]
            Time_End_B1.append(Time_End)
            Cost_B1.append(Cost)
            yield env.timeout(Duration_B1)
        elif NCBP_B1 == False and env.now == Time_End_B1[-1]:
            Revenue_B1.append(Revenue)
            Profit_B1.append(Profit)
            Time_Start_B1.append(Time_End_B1[-1])
            Team_ID_B4.append("B")
            Person_ID_B1.append("1")
            NCBP_B1 = True
            yield env.timeout(0)

def B2(env):
    global NCBP_B2
    while True:
        if NCBP_B2 == True:
            NCBP_B2 = False
            Duration_B2 = np.random.uniform(Team_B_Low, Team_B_High)
            Time_Taken_B2.append(Duration_B2)
            Time_End = Time_Taken_B2[-1] + Time_Start_B2[-1]
            Time_End_B2.append(Time_End)
            Cost_B2.append(Cost)
            yield env.timeout(Duration_B2)
        elif NCBP_B2 == False and env.now == Time_End_B2[-1]:
            Revenue_B2.append(Revenue)
            Profit_B2.append(Profit)
            Time_Start_B2.append(Time_End_B2[-1])
            Team_ID_B4.append("B")
            Person_ID_B2.append("2")
            NCBP_B2 = True
            yield env.timeout(0)

def B3(env):
    global NCBP_B3
    while True:
        if NCBP_B3 == True:
            NCBP_B3 = False
            Duration_B3 = np.random.uniform(Team_B_Low, Team_B_High)
            Time_Taken_B3.append(Duration_B3)
            Time_End = Time_Taken_B3[-1] + Time_Start_B3[-1]
            Time_End_B3.append(Time_End)
            Cost_B3.append(Cost)
            yield env.timeout(Duration_B3)
        elif NCBP_B3 == False and env.now == Time_End_B3[-1]:
            Revenue_B3.append(Revenue)
            Profit_B3.append(Profit)
            Time_Start_B3.append(Time_End_B3[-1])
            Team_ID_B4.append("B")
            Person_ID_B3.append("3")
            NCBP_B3 = True
            yield env.timeout(0)

def B4(env):
    global NCBP_B4
    while True:
        if NCBP_B4 == True:
            NCBP_B4 = False
            Duration_B4 = np.random.uniform(Team_B_Low, Team_B_High)
            Time_Taken_B4.append(Duration_B4)
            Time_End = Time_Taken_B4[-1] + Time_Start_B4[-1]
            Time_End_B4.append(Time_End)
            Cost_B4.append(Cost)
            yield env.timeout(Duration_B4)
        elif NCBP_B4 == False and env.now == Time_End_B4[-1]:
            Revenue_B4.append(Revenue)
            Profit_B4.append(Profit)
            Time_Start_B4.append(Time_End_B4[-1])
            Team_ID_B4.append("B")
            Person_ID_B4.append("4")
            NCBP_B4 = True
            yield env.timeout(0)

env = simpy.Environment()
people_a1 = simpy.Resource(env, capacity = 1)
people_a2 = simpy.Resource(env, capacity = 1)
people_a3 = simpy.Resource(env, capacity = 1)
people_a4 = simpy.Resource(env, capacity = 1)
env.process(A(env, people_a1, people_a2, people_a3, people_a4))
env.process(B1(env))
env.process(B2(env))
env.process(B3(env))
env.process(B4(env))
env.run(until = Time_Limit)