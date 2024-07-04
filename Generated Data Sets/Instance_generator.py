#### Code for the HFMDCVRPTW instance generator

## Import commands

import numpy as np
import matplotlib.pyplot as plt
from gurobipy import *
import pandas as pd
import sys
import random
import time

#import functions

## Parameters

def instance(dep_cap,stby_len,alpha,seed,clients,q,dep):
    rnd = np.random
    rnd.seed(seed)
    number_vehicles = len(q)
    CP6_clients = clients[0] # Number of clients to visit everyday
    CP3_clients = clients[1] # Number of clients to visit every two days
    CP2_clients = clients[2] # Number of clients to visit every three days
    CP1_clients = clients[3] # Number of clients to visit once
    cl = CP1_clients+CP6_clients+CP3_clients+CP2_clients # Number of clients
    days = 6 # Number of days
    n = cl + dep # Number of nodes

    # Coordinates generation
    
    xc = rnd.rand(cl + dep)*100-50 # x coordinates
    yc = rnd.rand(cl + dep)*50-25 # y coordinates
        
    # Fixating depots
        
    xc[0] = -25
    yc[0] = 0
        
    xc[1] = 25
    yc[1] = 0
    
    # Distance matrix generation
        
    t = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            t[i,j] = np.hypot(xc[i]-xc[j],yc[i]-yc[j])
            
    ## Plot
    
    plt.plot(xc[0],yc[0],c="r",marker="s")
    plt.scatter(xc[1],yc[1],c="r",marker="s")
    plt.scatter(xc[2:],yc[2:],c="b")
    for i in range(n):
        plt.annotate(i, (xc[i],yc[i]))
    
    F = [6,3,2,1] # Set of frequencies
    C = [i for i in range(dep,n)] # Set of clients
    CP6 = [i for i in range(dep,CP6_clients+dep)] # Set CP12
    CP3 = [i for i in range(CP6[-1]+1,CP6[-1]+CP3_clients+1)] # Set CP6
    CP2 = [i for i in range(CP3[-1]+1,CP3[-1]+CP2_clients+1)] # Set CP4
    CP1 = [i for i in range(CP2[-1]+1,CP2[-1]+CP1_clients+1)] # Set CP2
    CP = {
            6:CP6,
            3:CP3,
            2:CP2,
            1:CP1
        }
    P = {
        6:[0],
        3:[1,2],
        2:[3,4,5],
        1:[6,7,8,9,10,11]
        }
    NP = {
        6:[1,2,3,4,5,6,7,8,9,10,11],
        3:[0,3,4,5,6,7,8,9,10,11],
        2:[0,1,2,6,7,8,9,10,11],
        1:[0,1,2,3,4,5]
        }
    PforU = [i for i in range(0,12)]
    A = np.loadtxt("PatternShort.txt")
    D = [i for i in range(0,dep)] # Set of deposits
    N = D + C # Set of nodes
    H = [i for i in range(0,days)] # Set of days
    K = [i for i in range(0,number_vehicles)] # Set of vehicles
    
    # Demand
    
    dem = {i: rnd.randint(1,10) for i in C} # Random demand
    #dem = {i: 1 for i in C} # Random demand
    
    # Time to serve client c
    
    s = {i: rnd.randint(10,20) for i in C} # Random time service
    s[0]=0 # Adding times of service from depots
    s[1]=0 # Adding times of service from depots
    
    # Time windows
    
    tw_len = 120*alpha # Minutes of tw
    a = {i: rnd.randint(0,300-tw_len) for i in C} # Random initial tw
    a[0] = 0
    a[1] = 0
    b = {i: a[i]+tw_len for i in C} # Random initial tw
    b[0] = 300
    b[1] = 300
    
    # Stand-by time
    
    l = {i: stby_len for i in C} # Fixed stand-by time
    
    vis = {
        6:6,
        3:3,
        2:2,
        1:1
        }
    
    # Depot capacity
    
    R = dep_cap
    
    return(N,H,K,C,P,D,vis,R,t,s,dem,a,b,l,cl,n,days,number_vehicles,CP,PforU,F,A,NP)