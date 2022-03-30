import pandas as pd
from pathlib import Path
import os
import csv

data = pd.read_csv('C:\\Users\\gaura\\OneDrive\\Desktop\\Projects\\Chicago-Crime-Rate-Detection\Dataset\\Chicago_Crimes_2012_to_2017.csv', sep='delimiter')
df = data[1:100]
df.to_csv('Chicago_Crimes_2012_to_2017.csv')
