import pandas as pd
from mining import *
import os

dataset_dir = os.path.dirname(os.path.abspath(__file__)) + "\datasets" + "\malicious_urls.csv"
df = pd.read_csv(dataset_dir)

print(df.head())