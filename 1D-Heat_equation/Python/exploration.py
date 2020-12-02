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


# %%
#fig, ax = plt.subplots()
#sns.lineplot(data = fom, palette = 'rocket',ax = ax, ci = None) # first dataset
#sns.lineplot(data = rom, palette = "twilight", ax=ax, ci = None) # second dataset
fig, ax = plt.subplots(figsize = (10, 10))
camera = Camera(fig)

plt.xlim(0, 130)
plt.xlabel('x',fontsize=20)
plt.ylabel('Heat Rate (u)',fontsize=20)
plt.title('ROM Model Solution vs. FOM solution',fontsize=20)

for i in range(len(rom.columns) - 1):
    sns.set_style("white")
    sns.lineplot(data = fom.iloc[:,i], color = '#a9a9a9',ax = ax, ci = None) # first dataset
    sns.lineplot(data = rom.iloc[:,i], color = '#add8e6',ax = ax, ci = None)
    sns.despine()
    plt.legend(labels=['FOM', 'ROM'])

    #rom.iloc[:,i].plot(legend=False, color='#add8e6',linewidth=2, alpha=1, ax=ax)
    #fom.iloc[:,i].plot(legend=False, color='#a9a9a9',linewidth=2, alpha=1, ax=ax)
    camera.snap()

animation = camera.animate(interval = 50)
animation.save('models.gif')

# %%
# gettting a neat table comparing everything
m_type = ['FOM', 'ROM']
m_error = [0, np.sqrt(mean_squared_error(fom, rom))]
m_cost = [t_fom, t_rom]

comp_table = pd.DataFrame({'Model': m_type, 'RMSE': m_error, 'Cost': m_cost})
comp_table.to_csv('table.csv', index = False, encoding = 'utf-8')
# %%