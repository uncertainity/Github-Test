import numpy as np
import matplotlib.pyplot as plt
from numba import jit

dt = 0.001

def merchantShip(x,vm,run):
    dist = np.sqrt((vm[0]**2 + vm[1]**2))
    x_new = np.zeros(2)
    x_new[0] = x[0] + vm[0]*dt*(run/dist)
    x_new[1] = x[1] + vm[1]*dt*(run/dist)
    return x_new

t = np.arange(0,1,dt)
n = t.shape[0]

#m1 = np.zeros((2,n))
#initial_x = np.array([3,0])
#vm = np.array([0,1])
#run = 80
#for i in range(n):
#    x_new = merchantShip(initial_x,vm,run)
#    m1[:,i] = x_new
#    initial_x = x_new

#print(m1[:,-1:])
#plt.plot(m1[0],m1[1],"g--",color = "green")

def pirateShip(y,x,chase):
    vp = np.zeros(2)
    vp[0] = x[0] - y[0]
    vp[1] = x[1] - y[1] 
    dist = np.sqrt(vp[0]**2 + vp[1]**2)
    y_new = np.zeros(2)
    y_new[0] = y[0] + vp[0]*dt*(chase/dist)
    y_new[1] = y[1] + vp[1]*dt*(chase/dist)
    return y_new


def pursuit(initial_x,vm,initial_y,run,chase):
    m_loc = np.zeros((2,n))
    for i in range(n):
        x_new = merchantShip(initial_x,vm,run)
        m_loc[:,i] = x_new
        initial_x = x_new
    p_loc = np.zeros((2,n))
    for i in range(n):
        y_new = pirateShip(initial_y,m_loc[:,i],chase)
        p_loc[:,i] = y_new
        initial_y = y_new
    return m_loc,p_loc

initial_x = np.array([2,0])
vm = np.array([0,1])
run = 80
initial_y = np.array([0,0])
chase = 50
m_loc,p_loc = pursuit(initial_x,vm,initial_y,run,chase)
plt.plot(m_loc[0],m_loc[1],"g--",color = "green")
plt.plot(p_loc[0],p_loc[1],"g--",color = "red")

###  Variable Definitions ###
#initial_x --> initial position of the merchant ship (the runner)
#initial_y --> initial position of the pirate ship (the chaser)
#vm --> direction vector of the runner
#run --> speed of the runner
#chase --> speed of the chaser

    
    
    