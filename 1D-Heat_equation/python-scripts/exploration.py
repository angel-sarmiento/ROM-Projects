# This is just a notebook style doc where data exploration and plotting will be done
#!/usr/local/bin/ python3
#%% Library Imports
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
#import matplotlib.style as style, style.available
from celluloid import Camera


from compare_fom_rom import *

# %% Getting relevant info from compare_fom_rom.py
mu = 0.1

fom, rom, t_fom, t_rom = compare_FOM_ROM(phi, mu)

# %% Creating a nice gif showing model with POD basis of 5 dimensions

fig, ax = plt.subplots(figsize = (10, 10))
camera = Camera(fig)

plt.xlim(0, 130)
plt.xlabel('x',fontsize=20)
plt.ylabel('Heat Rate (u)',fontsize=20)
plt.title('ROM Model Solution vs. FOM solution of the 1D Heat Equation',fontsize=20)

for i in range(len(rom.columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom.iloc[:,i], color = '#a9a9a9',ax = ax, ci = None) # first dataset
    sns.lineplot(data = rom.iloc[:,i], color = '#add8e6',ax = ax, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])
    camera.snap()

animation = camera.animate(interval = 50)
animation.save('images/models.gif')


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



# %% Comparing different mu values
# gettting a neat table comparing everything
m_type = ['FOM', 'ROM', 'ROM_2', 'ROM_3', 'ROM_4']
m_error = [0, np.sqrt(mean_squared_error(fom, rom)), np.sqrt(mean_squared_error(fom_new[0], rom_new[0])), np.sqrt(mean_squared_error(fom_new[1], rom_new[1])), np.sqrt(mean_squared_error(fom_new[2], rom_new[2]))]
#mu values 
m_mu = [mu, mu, mu_new[0], mu_new[1], mu_new[2]]
m_cost = [t_fom, t_rom, t_rom_new[0], t_rom_new[1], t_rom_new[2]]
t_saved = [t_fom - t_fom, t_fom - t_rom, t_fom_new[0] - t_rom_new[0], t_fom_new[1] - t_rom_new[1], t_fom_new[2] - t_rom_new[2]]

# creating the comparison table and then exporting to csv
comp_table = pd.DataFrame({'model': m_type, 'mu': m_mu, 'RMSE': m_error, 'time': m_cost, 'time_saved': t_saved})
comp_table.to_csv('data/table.csv', index = False, encoding = 'utf-8')


#%% Plotting the different Mu values in a 2x2 grid







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



# %% Comparing different POD bases with a table

n_dim = [128, (phi_new[0].shape)[1], (phi_new[1].shape)[1], (phi_new[2].shape)[1], (phi_new[3].shape)[1]]
p_error = [0, np.sqrt(mean_squared_error(fom_npod[0], rom_npod[0])), np.sqrt(mean_squared_error(fom_npod[1], rom_npod[1])), np.sqrt(mean_squared_error(fom_npod[2], rom_npod[2])), np.sqrt(mean_squared_error(fom_npod[3], rom_npod[3]))]

# creating the table, not creating the time elapsed this time
pod_table = pd.DataFrame({'model': m_type, 'n_dim': n_dim, 'RMSE': p_error})
pod_table.to_csv('data/pod_new_bases.csv', index = False, encoding='utf-8')


# %% Bar Graph comparing RMSE

sub_table = pod_table[1:]

sns.set(rc={'figure.figsize':(8,6)})
sns.set_theme(style="whitegrid")
bar_plot = sns.barplot(x="RMSE", y="model", hue = "n_dim", data=sub_table)
plt.title("POD Bases Dimensions and Their Effect on Accuracy")
plt.xlabel("RMSE")
plt.ylabel("Model")

bar_plot.get_figure().savefig('images/pod_bar.png')
#%% animated plot of new POD bases

