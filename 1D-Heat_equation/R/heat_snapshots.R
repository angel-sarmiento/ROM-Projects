## Florida Polytechnic University
## Angel Sarmiento

## This is the main function implemented in developing a solution to the 1D heat equation 
## using the BTCS Scheme for use in ROM

t_end = 1                 # Simulation time in seconds
n = 129                   # Discretization in space
nt = 129                  # time-step

dx = 1/n
dt = t_end/nt
x = c(0:dx:1)

heat_snapshots <- function(snapshots_matrix, U, S, V){
  
}