from the_well.data import WellDataset
from torch.utils.data import DataLoader

trainset = WellDataset(
    well_base_path=""
    well_dataset_name=""
    well_split_name="train"
)