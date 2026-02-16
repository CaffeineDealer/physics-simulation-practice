#%%
from the_well.data import WellDataset
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from IPython import display
import numpy as np

trainset = WellDataset(
    well_base_path="./data/datasets/",
    well_dataset_name="active_matter",
    well_split_name="train")

train_loader = DataLoader(trainset)

#%%
batch = next(iter(train_loader))
print(batch.keys())
data = batch['input_fields']
# %%
data = np.squeeze(data)
n1, n2, n3 = data.shape

fig, ax = plt.subplots(figsize=(15, 8))

for i in range(n3):
    ax.clear()
    ax.imshow(data[:, :,i])
    fig.canvas.draw()
    display.display(fig)  
    display.clear_output(wait=True)
    plt.pause(0.1)  
plt.show()