# %%
from pybaseball import schedule_and_record
import time
import os
import numpy as np


TEAMS = [
    'ARI', 'ATL', 'BAL', 'BOS', 'CHC',
    'CHW', 'CIN', 'CLE', 'COL', 'DET',
    'HOU', 'KCR', 'ANA', 'LAD', 'FLA',
    'MIL', 'MIN', 'NYM', 'NYY', 'OAK',
    'PHI', 'PIT', 'SDP', 'SFG', 'SEA',
    'STL', 'TEX', 'TBR', 'TOR', 'WSN',
    'MON',  # until 2004
    'TBD',  # until 2007
]

YEARS = np.arange(2000, 2024)


# SCRAPE DATA
for year in YEARS:
    for team in TEAMS:
        # download if not already exists
        if not os.path.isfile(os.path.join('data', 'schedule_and_record', f'{year}_{team}.csv')):
            try:
                data = schedule_and_record(year, team)
                data.to_csv(os.path.join(
                    'data', 'schedule_and_record', f'{year}_{team}.csv'))
                print(f'{year}-{team} done.')
            except Exception:
                print(f'ERROR! {year}-{team} not available')

            # wait to not get blocked
            time.sleep(10)

        else:
            print(f'{year}_{team}.csv already exists. skipping')
