## Florida Polytechnic University
## Angel Sarmiento

## This is the main function implemented in developing a solution to the 1D heat equation 
## using the BTCS Scheme for use in ROM
#!/usr/local/bin/ python3
#%% Importing libraries
import scipy as sp
import scipy.sparse as sps
from scipy.sparse import spdiags, linalg, diags, csr_matrix
import numpy as np
from numpy import cos, sin, pi
import pandas as pd

#%% Defining the function

def heat_snapshots():
    snapshots_matrix = pd.DataFrame()
    

    t_end = 1                 # Simulation time in seconds
    n = 129                   # Discretization in space
    nt = 129                  # time-step
    mu = 0.1                  # heat equation constant

    dx = 1/n
    dt = t_end/nt
    x = np.arange(0, 1, dx).transpose()


    # INITIAL CONDITIONS 
    initial_cond = np.array([cos(3*pi*x/2), sin(3*pi*x/2), 3*cos(5*pi*x/2), 2*sin(pi*x/2), 7*cos(5*pi*x/2)]).transpose()
    initial_val = np.array([1, 0.5, 3, 0.7, 1.5]).transpose()    

    # for loop for iteration  
    for i in range(0, len(initial_val)):
        
        u = initial_cond[:, i]              #heat-transfer function u at initial time
        u[0] = initial_val[i]               #value of u at initial position

        #Setting up the (n-1) x (n-1) coefficient matrix.
        e = np.ones((n-1, 1))
        m = mu*dt/dx**2
        # creating a matrix of diagonals
        A = spdiags((e * np.array([-m, 1+2*m, -m])).transpose(), [-1, 0 , 1], n-1, n-1)

        #fixing lower right entry for Neuman Boundary Condition
        A = csr_matrix(A)
        A[n-2, n-2] = 1 + m

        # nested time loop to calculate and then apply the new rhs/lhs in BTCS
        for j in range(nt):
            #time = j*dt
            #setting the right hand side
            rhs = u[1:len(u)]                   # this is to not overwrite the boundary condition accidentally
            rhs[0] = rhs[0] + m*u[0]        # fixing the first equation for the boundary condition
            
            u_new = sps.linalg.spsolve(A, rhs)    # getting the new rhs by solving A\b

            u[1:len(u)] = u_new
            #u[-1] = u[-2]                  #This just fixes the Neumann Boundary condition if we wanted to plot

            # collecting the snapshots 
            if j % 5 == 0: 
                snapshots_matrix = pd.concat([snapshots_matrix, pd.DataFrame(u[0:-1])], axis = 1)
    
    # computing the svd for the snapshots matrix and returning them 
    U, S, V = np.linalg.svd(snapshots_matrix, full_matrices=True)  

    return snapshots_matrix, U, S, V
