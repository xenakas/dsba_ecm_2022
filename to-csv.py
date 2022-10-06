#!/bin/python3.9
import glob
import pandas as pd
import os
for file in glob.glob('**/*.xls', recursive=True):
    data = pd.read_excel(file)
    data.to_csv(os.path.splitext()[0] + '.csv')

