#This is code to get the different plots for different values of mu
#%% importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
from celluloid import Camera


from compare_fom_rom import *


# %% Getting relevant info from compare_fom_rom.py
mu = 0.1

fom, rom, t_fom, t_rom = compare_FOM_ROM(phi, mu)



#%% Iterating over multiple values of mu?
mu_new = [0.4, 1.8, 2]

#creating empty lists to append to 
fom_new = []
rom_new = []
t_fom_new = []
t_rom_new = []

#for loop to solve both the ROM and FOM and append those same values to lists
# this essentially creates a list of dataframes to have their index called later
for j in range(len(mu_new)):
    fom_it, rom_it, t_fom_it, t_rom_it = compare_FOM_ROM(phi, mu_new[j])

    fom_new.append(fom_it)
    rom_new.append(rom_it)
    t_fom_new.append(t_fom_it)
    t_rom_new.append(t_rom_it)




# %% Creating a nice gif showing model with POD basis of 4 dimensions

fig, ax = plt.subplots(figsize = (8, 8))
camera = Camera(fig)



for i in range(len(rom.columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom.iloc[:,i], color = '#a9a9a9',ax = ax, ci = None) # first dataset
    sns.lineplot(data = rom.iloc[:,i], color = '#add8e6',ax = ax, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    plt.xlim(0, 130)
    plt.xlabel('x')
    plt.ylabel('Heat Rate (u)')
    plt.title('ROM vs. FOM of the 1D Heat Equation',fontsize=16)
    camera.snap()


animation = camera.animate(interval = 50)
animation.save('images/models.gif', dpi = 150)




#%% Plot 2




fig2, ax2 = plt.subplots(figsize = (8, 8))
camera2 = Camera(fig2)



for i in range(len(rom.columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom_new[0].iloc[:,i], color = '#a9a9a9',ax = ax2, ci = None) # first dataset
    sns.lineplot(data = rom_new[0].iloc[:,i], color = '#CC0000',ax = ax2, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    plt.xlim(0, 130)
    plt.xlabel('x')
    plt.ylabel('Heat Rate (u)')
    plt.title('ROM vs. FOM of the 1D Heat Equation; mu = ' + str(mu_new[0]),fontsize=16)
    camera2.snap()


animation2 = camera2.animate(interval = 50)
animation2.save('images/mu_plot_1.gif', dpi = 150)

#----------------------------------------------------------------------------------------------------
#%% Plot 3

fig3, ax3 = plt.subplots(figsize = (8, 8))
camera3 = Camera(fig3)



for i in range(len(rom.columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom_new[1].iloc[:,i], color = '#a9a9a9',ax = ax3, ci = None) # first dataset
    sns.lineplot(data = rom_new[1].iloc[:,i], color = '#add8e6',ax = ax3, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    plt.xlim(0, 130)
    plt.xlabel('x')
    plt.ylabel('Heat Rate (u)')
    plt.title('ROM vs. FOM of the 1D Heat Equation; mu = ' + str(mu_new[1]),fontsize=16)
    camera3.snap()


animation3 = camera3.animate(interval = 50)
animation3.save('images/mu_plot_2.gif', dpi = 150) 

#----------------------------------------------------------------------------------------------------
#%% Plot 4
fig4, ax4 = plt.subplots(figsize = (8, 8))
camera4 = Camera(fig4)



for i in range(len(rom.columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom_new[2].iloc[:,i], color = '#a9a9a9',ax = ax4, ci = None) # first dataset
    sns.lineplot(data = rom_new[2].iloc[:,i], color = '#add8e6',ax = ax4, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    plt.xlim(0, 130)
    plt.xlabel('x')
    plt.ylabel('Heat Rate (u)')
    plt.title('ROM vs. FOM of the 1D Heat Equation; mu = ' + str(mu_new[2]),fontsize=16)
    camera4.snap()


animation4 = camera4.animate(interval = 50)
animation4.save('images/mu_plot_3.gif', dpi = 150) 

