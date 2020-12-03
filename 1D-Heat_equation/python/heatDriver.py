# calling the full-order model and getting the snapshots matrix and new basis via SVD
# Then comparing ROM solution with FOM solution. 
# importing necessary libraries
#!/usr/local/bin python3
from generate_snapshots import *
from compare_fom_rom import *

# from heat_snapshots.py
snapshots_matrix, U, S, V   = heat_snapshots()

# from compare_FOM_ROM.py
fom, rom, t_fom, t_rom = compare_FOM_ROM(phi)

pd.DataFrame(snapshots_matrix).to_csv("data/snapshots.csv")


