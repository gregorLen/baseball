from pybaseball import statcast
import numpy as np
import os

YEARS = np.arange(2015, 2024)
PATH = os.path.join('data', 'statcast')

if __name__ == "__main__":
    for year in YEARS:
        file_path = PATH + f'/{year}.csv'
        if not os.path.isfile(file_path):
            data = statcast(f'{year}-01-01', f'{year}-12-31')
            data.to_csv(file_path)
        else:
            print(f'{file_path} already exists. skipping')
