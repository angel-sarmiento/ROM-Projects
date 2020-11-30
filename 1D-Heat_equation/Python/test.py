#%%
# %%
for j in range(129):
    print(j)
# %%

initial_val = [1, 2, 4, 5, 6, 7]
for i in range(0, len(initial_val)):
        print(i)
        # nested time loop to calculate and then apply the new rhs/lhs in BTCS
        for j in range(129):
            
            # collecting the snapshots 
            print(j)
            #if j % 5 == 0:
            #    snapshots_matrix = np.append(snapshots_matrix, u[0:-1], axis = 0)
            #else:
            #    break
    # computing the svd for the snapshots matrix and returning them 
#    U, S, V = np.linalg.svd(snapshots_matrix)
# %%
import numpy as np 
initial_val = np.array([1, 0.5, 3, 0.7, 1.5]).transpose()    
len(initial_val)
# %%
