#calling the full-order model and getting the snapshots matrix and new basis via SVD
# importing necessary libraries
#!/usr/local/bin python3
from generate_snapshots import *

snapshots_matrix, u, s, vh, snapshots_list  = heat_snapshots()

#print(u)
#print(s)
print(vh)

