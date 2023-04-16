# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import glob


def get_mins(time_str):
    h, m = time_str.split(':')
    return int(h) * 60 + int(m)


ALL_FILES = glob.glob(os.path.join('data', 'schedule_and_record', '*.csv'))
IMG_PATH = os.path.join('img', 'game time')


li = []
for file in ALL_FILES:
    df = pd.read_csv(file, index_col=0, header=0)
    # only home games (avoid double counting)
    df = df[df['Home_Away'] == 'Home']
    # ONLY games  9.0 Innings
    # df = df[df["Inn"]== 9.0]
    df = df[df["Inn"] >= 9.0]

    year = file.split('/')[2][:4]
    df.insert(1, 'Year', year)
    df = df[~df['Time'].isna()]
    li.append(df)
# concat
data = pd.concat(li, axis=0, ignore_index=True)
data['Time'] = data['Time'].apply(get_mins)
data = data.sort_values('Year')


# %%
# data.sort_values('Time', ascending=True).iloc[:,:10]
ts_mean = data[['Year', 'Time']].groupby('Year').mean()
ts_median = data[['Year', 'Time']].groupby('Year').median()
ts_std = data[['Year', 'Time']].groupby('Year').std()

# %%
sns.set_style('whitegrid')  # whitegrid, darkgrid
sns.set_context("paper")  # paper, talk, poster
plt.figure(figsize=(10, 5))
g = sns.lineplot(data=data,
                 x="Year",
                 y="Time",
                 marker="o",
                 dashes=False,
                 errorbar='pi',
                 )
g.set(ylabel="Time in Minutes")
g.set(ylim=(0, None))
plt.title('Game Length (9 Innings)')
plt.savefig(IMG_PATH + '/lineplot.pdf')

# %%
g = sns.catplot(data=data,
            x='Year',
            y='Time',
            height=5,
            aspect=2.0,
            alpha = 0.6
            )
g.fig.suptitle('Game Length (9 Innings)')
g.despine(left=True)
g.set(ylabel="Time in Minutes")
g.set(ylim=(0, None))
plt.savefig(IMG_PATH + '/catplot.pdf')


# %%
g = sns.catplot(data=data,
            x='Year',
            y='Time',
            kind = 'bar',
            color='dimgray',
            width=1.0,
            height=5,
            aspect=2.0,
            errorbar='pi'
            )
# plt.title('Game Length (9 Innings)')
g.fig.suptitle('Game Length (9 Innings)')
g.despine(left=True)
g.set(ylabel="Time in Minutes")
g.set(ylim=(0, None))
plt.savefig(IMG_PATH + '/barplot.pdf')


# %%
g = sns.catplot(data=data,
            x='Year',
            y='Time',
            height=5,
            aspect=2.0,
            kind='boxen'
            )
# plt.title('Game Length (9 Innings)')
g.fig.suptitle('Game Length (9 Innings)')
g.set(ylim=(0, None))
g.despine(left=True)
g.set(ylabel="Time in Minutes")
plt.savefig(IMG_PATH + '/boxenplot.pdf')

# %%
fig = plt.figure(figsize=(10,5))
sns.set_style('whitegrid')
# sns.set(style="nogrid")
plt.plot(ts_median,
         linestyle='dotted',
         marker='o',
         markersize=8
         )
sns.despine(left=True)
plt.title("Median Game Length (9 Innings)")
plt.xlabel("Year")
plt.ylabel("Time in Minutes")
plt.xticks(['2000', '2005', '2010', '2015', '2020', '2023'])
plt.show()
fig.savefig(IMG_PATH + "/median.pdf")
# %%
