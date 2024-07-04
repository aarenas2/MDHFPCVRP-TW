#### Data set generation for the MDHFPCVRP-TW

## Imports

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import random
import Instance_generator

## Model's conditions

www = 1 # Size of the problem
dense = 1 # d in file inst_guide
balanced = 0 # b in file inst_guide
sparse = 0 # s in file inst_guide
seed = 0 # Seed used

# Automated conditions

dep_cap = [(20)*www,(20)*www] # Depot's capacity
stby_len = 30 # Max stand-by time in every client
alpha = 1 # Time windows scaling
dep = 2 # Number of depots

# The following cycle sets the vehicles' distribution

if www == 1:
    q = [12,12,16] # Vehicles distribution
elif www == 2:
    q = [12,12,12,12,16,16] # Vehicles distribution
elif www == 3:
    q = [12,12,12,12,12,12,16,16,16] # Vehicles distribution
else:
    q = [12,12,12,12,12,12,12,12,16,16,16,16] # Vehicles distribution
    
# The following cycle sets the clients' distribution

if dense == 1:
    clients = [3*www,4*www,1,1] # Clients' distribution
if balanced == 1:
    clients = [2*www,3*www,3*www,3*www] # Clients' distribution
if sparse == 1:
    clients = [1*www,4*www,4*www,4*www] # Clients' distribution


N,H,K,C,P,D,vis,R,t,s,dem,a,b,l,cl,n,days,number_vehicles,CP,PforU,F,A,NP = Instance_generator.instance(dep_cap,stby_len,alpha,seed,clients,q,dep)



