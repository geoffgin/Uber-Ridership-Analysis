import os
import kaggle
import pandas as pd
import zipfile

def download_kaggle_dataset(dataset, path, file_names):
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset, path=path, unzip=False)
    
    with zipfile.ZipFile(os.path.join(path, f"{dataset.split('/')[-1]}.zip"), 'r') as z:
        for file_name in file_names:
            z.extract(file_name, path=path)
    
    print(f"Downloaded specified files from dataset {dataset} to {path}")
    return [pd.read_csv(os.path.join(path, file_name)) for file_name in file_names]

def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created directory {dir_path}")
    else:
        print(f"Directory {dir_path} already exists")

# Kaggle dataset path
dataset_path = "fivethirtyeight/uber-pickups-in-new-york-city"

# Local directory to save the dataset
local_dir = "./assets"

# File names to load
file_names = [
    'uber-raw-data-apr14.csv',
    'uber-raw-data-may14.csv',
    'uber-raw-data-jun14.csv',
    'uber-raw-data-jul14.csv',
    'uber-raw-data-aug14.csv',
    'uber-raw-data-sep14.csv'
]

# Create the 'uber_data' directory if it doesn't exist
create_directory(local_dir)

# Download the specified files from the dataset to the 'uber_data' directory and load them
datasets = download_kaggle_dataset(dataset_path, local_dir, file_names)