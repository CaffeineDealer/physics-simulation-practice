#%%
import h5py
import matplotlib.pyplot as plt

with h5py.File("./data/datasets/active_matter/data/train/active_matter_L_10.0_zeta_1.0_alpha_-2.0.hdf5",'r') as f:
    print(f.keys())
    data = f['t0_fields']['concentration'][:]
print(data.shape)

#%%
from IPython import display

n1, n2, n3, n4 = data.shape

fig, axes = plt.subplots(2, 2, figsize=(15, 8))
axes = axes.flatten()

for i in range(n2):
    for j in range(n1):
        axes[j].clear()
        axes[j].imshow(data[j, i, :, :])
    fig.canvas.draw()
    # plt.pause(0.001)  
    display.display(fig)  
    display.clear_output(wait=True) 

plt.show()
# %%
