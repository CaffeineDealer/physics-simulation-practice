from the_well.data import WellDataset
from torch.utils.data import DataLoader

trainset = WellDataset(
    well_base_path="./data/datasets/",
    well_dataset_name="active_matter",
    well_split_name="train"
)

train_loader = DataLoader(trainset)
