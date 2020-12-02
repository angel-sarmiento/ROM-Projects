# THis is an algorithmic implementation of a POD Reduced order model vs. a Full-order model 
# of a simple heat equation (1D). The full-order model is calculated using a BTCS scheme, with 
# Neumann and Dirichlet boundary conditions

#
#            u_t = mu * u_xx    for 0 <= x <= 1
#            u(0,t)   = 1
#            u_x(1,t) = 0
#            u(x,0)   = cos(3*pi*x/2)
#

#%% Importing libraries
import scipy as sp
import scipy.sparse as sps
from scipy.sparse import spdiags, linalg, diags, csr_matrix
import numpy as np
from numpy import cos, sin, pi
import pandas as pd

#time elapsed stuff
from tic_toc_snapshot import * 

#setting seed for reproducibility
import random
random.seed(123)

#%% importing the snapshot matrix

data = pd.read_csv("data/heat_snapshots.csv", header = None)


#%% Assigning some variables Globally, as well as initial conditions 
t_end = 1                 # Simulation time in seconds
n = 129                   # Discretization in space
nt = 129                  # time-step
#mu = 0.1                  # heat equation constant

dx = 1/n
dt = t_end/nt
x = np.arange(0, 1, dx).transpose()

#INITIAL CONDITIONS
#This can be changed right here without needed to edit the function itself (hopefully)
u = cos(3*pi*x/2)
v = cos(3*pi*x/2)
u[0] = 1   
v[0] = 1

# %% Performing SVD to get POD basis 

#Big U is the left singular vectors. This is not to be confused with small u
U, S, V = np.linalg.svd(data, full_matrices=True)

#New POD Basis
phi = U[:, :4]

# %% Function, compare_FOM_ROM
def compare_FOM_ROM(phi, mu):
    #getting a value for mu 
    mu = mu

    #Setting up u for both ROM and FOM
    u_FOM = u
    u_ROM = v

    # time
    time_FOM = []
    time_ROM = []

    #Setting up the (n-1) x (n-1) coefficient matrix.
    e = np.ones((n-1, 1))
    m = mu*dt/dx**2
    # creating a matrix of diagonals
    A = spdiags((e * np.array([-m, 1+2*m, -m])).transpose(), [-1, 0 , 1], n-1, n-1)

    #fixing lower right entry for Neuman Boundary Condition
    A = csr_matrix(A)
    A[n-2, n-2] = 1 + m

    #THIS MAY NEED TO BE ADJUSTED
    # setting up blank arrays to be appended to later
    big_u_FOM = pd.DataFrame()
    big_u_ROM = pd.DataFrame()

    big_a_FOM = A
    #might need to be transposed
    big_a_ROM = phi.transpose()*A@phi

    
    #Setting up the time loop 
    for i in range(1, nt):
        
        # setting the rhs for the FOM
        rhs = u_FOM[1:]                   
        rhs[0] = rhs[0] + m*u_FOM[0]        # fixing the first equation for the boundary condition
        rhs_FOM = rhs 
        
        #FOM solution
        tic()
        u_FOM_new = sps.linalg.spsolve(big_a_FOM, rhs_FOM)    # getting the new rhs by solving A\b
        #recording time elapsed
        t_FOM = toc()
        
        u_FOM[1:] = u_FOM_new
        #u_FOM[-1] = u_FOM[-2]                   # fixing neumann BC
        
        #ROM solution 
        # Same for the ROM
        rhs_red = u_ROM[1:]
        rhs_red[0] = rhs_red[0] + m*u_ROM[0]
        
        
        tic()
        rhs_ROM = phi.transpose()@rhs_red
        u_ROM_sol = sps.linalg.spsolve(big_a_ROM, rhs_ROM)
        u_ROM_new = phi@u_ROM_sol
        #recording time elapsed
        t_ROM = toc()

        u_ROM[1:] = u_ROM_new
        #u_ROM[-1] = u_ROM[-2]                   # fixing newmann BC again
        

        #adding the time elapsed values to a list
        time_FOM.append(t_FOM)
        time_ROM.append(t_ROM)
        
        #getting the final model solutions 
        big_u_FOM = pd.concat([big_u_FOM, pd.DataFrame(u_FOM)], axis = 1)
        big_u_ROM = pd.concat([big_u_ROM, pd.DataFrame(u_ROM)], axis = 1)
        
    #summing up the time taken for each approach
    tot_time_FOM = sum(time_FOM)
    tot_time_ROM = sum(time_ROM)

    return big_u_FOM, big_u_ROM, tot_time_FOM, tot_time_ROM
    