#This is code to get the different plots for different POD bases
#%% importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
from celluloid import Camera

from compare_fom_rom import *

# %% Comparing different POD bases 
phi_new = []

#iteratively getting new pod bases 
for k in range(4, 8):
    phi_new.append(U[:, :k])


# assigning lists like before
# each output parameter returned by compare_FOM_ROM
fom_npod = []
rom_npod = []
t_fom_npod = []
t_rom_npod = []

#for loop to solve ROM and FOM with different POD bases
for l in range(len(phi_new)):

    fom_npod_it, rom_npod_it, t_fom_nit, t_rom_nit = compare_FOM_ROM(phi_new[l], mu=0.1)

    fom_npod.append(fom_npod_it)
    rom_npod.append(rom_npod_it)
    t_fom_npod.append(t_fom_nit)
    t_rom_npod.append(t_rom_nit)

#%% Plots

fig, ax = plt.subplots(figsize = (8, 8))
camera = Camera(fig)



for i in range(len(rom_npod[0].columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom_npod[0].iloc[:,i], color = '#a9a9a9',ax = ax, ci = None) # first dataset
    sns.lineplot(data = rom_npod[0].iloc[:,i], color = '#fdad5c',ax = ax, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    plt.xlim(0, 130)
    plt.xlabel('x')
    plt.ylabel('Heat Rate (u)')
    plt.title('ROM vs. FOM of the 1D Heat Equation; # of Dimensions = ' + str((phi_new[0].shape)[1]),fontsize=16)
    camera.snap()


animation = camera.animate(interval = 50)
animation.save('images/pod_b1.gif', dpi = 150)


#----------------------------------------------------------------------------------------------------
#%% Plot 2

fig2, ax2 = plt.subplots(figsize = (8, 8))
camera2 = Camera(fig2)



for i in range(len(rom_npod[0].columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom_npod[1].iloc[:,i], color = '#a9a9a9',ax = ax2, ci = None) # first dataset
    sns.lineplot(data = rom_npod[1].iloc[:,i], color = '#fdad5c',ax = ax2, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    plt.xlim(0, 130)
    plt.xlabel('x')
    plt.ylabel('Heat Rate (u)')
    plt.title('ROM vs. FOM of the 1D Heat Equation; # of Dimensions = ' + str((phi_new[1].shape)[1]),fontsize=16)
    camera2.snap()


animation2 = camera2.animate(interval = 50)
animation2.save('images/pod_b2.gif', dpi = 150)

#----------------------------------------------------------------------------------------------------
#%% Plot 3

fig3, ax3 = plt.subplots(figsize = (8, 8))
camera3 = Camera(fig3)


for i in range(len(rom_npod[0].columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom_npod[2].iloc[:,i], color = '#a9a9a9',ax = ax3, ci = None) # first dataset
    sns.lineplot(data = rom_npod[2].iloc[:,i], color = '#fdad5c',ax = ax3, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    plt.xlim(0, 130)
    plt.xlabel('x')
    plt.ylabel('Heat Rate (u)')
    plt.title('ROM vs. FOM of the 1D Heat Equation; # of Dimensions = ' + str((phi_new[2].shape)[1]),fontsize=16)
    camera3.snap()


animation3 = camera3.animate(interval = 50)
animation3.save('images/pod_b3.gif', dpi = 150)

#----------------------------------------------------------------------------------------------------
#%% Plot 4

fig4, ax4 = plt.subplots(figsize = (8, 8))
camera4 = Camera(fig4)


for i in range(len(rom_npod[0].columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom_npod[3].iloc[:,i], color = '#a9a9a9',ax = ax4, ci = None) # first dataset
    sns.lineplot(data = rom_npod[3].iloc[:,i], color = '#0000CC',ax = ax4, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    plt.xlim(0, 130)
    plt.xlabel('x')
    plt.ylabel('Heat Rate (u)')
    plt.title('ROM vs. FOM of the 1D Heat Equation; # of Dimensions = ' + str((phi_new[3].shape)[1]),fontsize=16)
    camera4.snap()


animation4 = camera4.animate(interval = 50)
animation4.save('images/pod_b4.gif', dpi = 150)

