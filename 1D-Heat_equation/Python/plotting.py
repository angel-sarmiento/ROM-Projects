# This is just a notebook style doc where data exploration and plotting will be done
#!/usr/local/bin/ python3
#%% Library Imports
import seaborn as sns
import matplotlib.pyplot as plt
from compare_fom_rom import *

# %% Getting relevant info from compare_fom_rom.py

fom, rom, t_fom, t_rom = compare_FOM_ROM(phi)

# %% Plotting some graphs with animations



# %%
fig, ax = plt.subplots()
sns.lineplot(data = fom, palette = 'rocket',ax = ax, ci = None) # first dataset
sns.lineplot(data = rom, palette = "twilight", ax=ax, ci = None) # second dataset
# %%
