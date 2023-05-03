import pandas as pd
from mining import *
import os

dataset_folder = "\datasets"
dataset_file = "\malicious_urls.csv"

print(os.name)

if os.name != 'nt':
    dataset_folder = "/datasets"
    dataset_file = "/malicious_urls.csv"

dataset_dir = os.path.dirname(os.path.abspath(__file__)) + dataset_folder + dataset_file
df = pd.read_csv(dataset_dir)

print(df.head())