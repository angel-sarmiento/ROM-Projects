# This is just a notebook style doc where data exploration and plotting will be done
#!/usr/local/bin/ python3
#%% Library Imports
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
#import matplotlib.style as style, style.available
from celluloid import Camera

#setting seed for reproducibility
import random
random.seed(123)

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

# %% Comparing different mu values
# gettting a neat table comparing everything
m_type = ['FOM', 'ROM', 'ROM_2', 'ROM_3', 'ROM_4']
m_error = [0, np.sqrt(mean_squared_error(fom, rom))] 
#lambda function to get all of the respective RMSE values
m_error.extend(map(lambda x, y: np.sqrt(mean_squared_error(x, y)), fom_new, rom_new))


#mu values 
m_mu = [mu, mu, mu_new[0], mu_new[1], mu_new[2]]

#getting the time taken to run each model
m_cost = [t_fom, t_rom, t_rom_new[0], t_rom_new[1], t_rom_new[2]]

#time saved
t_saved = [t_fom - t_fom, t_fom - t_rom]
#lambda function to get the rest
t_saved.extend(map(lambda x, y: x - y, t_fom_new, t_rom_new))

# creating the comparison table and then exporting to csv
comp_table = pd.DataFrame({'model': m_type, 'mu': m_mu, 'RMSE': m_error, 'time': m_cost, 'time_saved': t_saved})
comp_table.to_csv('data/mu_tests_rom.csv', index = False, encoding = 'utf-8')


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

    fom_npod_it, rom_npod_it, t_fom_nit, t_rom_nit = compare_FOM_ROM(phi_new[l], mu_i=0.4)

    fom_npod.append(fom_npod_it)
    rom_npod.append(rom_npod_it)
    t_fom_npod.append(t_fom_nit)
    t_rom_npod.append(t_rom_nit)



# %% Comparing different POD bases with a table
m_type_p = ['FOM', 'ROM', 'ROM_2', 'ROM_3', 'ROM_4']


# this gets the number of dimensions from each of the models in the list phi_new
n_dim = [128]
# lambda function to get all of the dimensions through each 
n_dim.extend(map(lambda x: x.shape[1], phi_new))

#this of course gets the RMSE of each model 
p_error = [0]
p_error.extend(map(lambda x, y: np.sqrt(mean_squared_error(x, y)), fom_npod, rom_npod))

# getting the time taken
basis_time = [t_fom_npod[0]]
basis_time.extend(t_rom_npod)

# creating the table, not creating the time elapsed this time
pod_table = pd.DataFrame({'model': m_type_p, 'n_dim': n_dim, 'RMSE': p_error, 'time': basis_time})
pod_table.to_csv('data/pod_new_bases.csv', index = False, encoding='utf-8')


# %% Bar Graph comparing RMSE

sub_table = pod_table[1:]

sns.set(rc={'figure.figsize':(8,6)})
sns.set_theme(style="whitegrid")
bar_plot = sns.barplot(x="RMSE", y="model", hue = "n_dim", data=sub_table)
plt.title("POD Bases Dimensions and Their Effect on Accuracy")
plt.xlabel("RMSE")
plt.ylabel("Model")
sns.despine(bottom=True)

bar_plot.get_figure().savefig('images/pod_bar.png')
