"""
converts csv data in data frames and prelim stats analysis
"""

def days_dataframes():
     import pandas as pd
     days_df = pd.read_csv('days.csv')
     print days_df
     return days_df
days_df = days_dataframes()

import pandas as pd
days_df = days_df.transpose()
print days_df.describe()



def month_dataframes():
     import pandas as pd
     month_df = pd.read_csv('month.csv')
     print month_df
     return month_df
month_df = month_dataframes()

import pandas as pd
month_df = month_df.transpose()
print month_df.describe()



def week_dataframes():
     import pandas as pd
     week_df = pd.read_csv('week.csv')
     print week_df
     return week_df
week_df = week_dataframes()

import pandas as pd
week_df = week_df.transpose()
print week_df.describe()



def hour_dataframes():
     import pandas as pd
     hour_df = pd.read_csv('hour.csv')
     print hour_df
     return hour_df
hour_df = hour_dataframes()

import pandas as pd
hour_df = hour_df.transpose()
print hour_df.describe()

def hour_spd_df():
     import pandas as pd
     hour_spd = pd.read_csv('hour_avgspeed.csv')
     print hour_spd
     return hour_spd
hour_spd = hour_spd_df()

def direction_dataframes():
     import pandas as pd
     direction_df = pd.read_csv('direction.csv')
     print direction_df
     return direction_df
direction_df = direction_dataframes()

import pandas as pd
direction_df = direction_df.transpose()
print direction_df.describe()


days_dataframes()
month_dataframes()
week_dataframes()
hour_dataframes()
direction_dataframes()
     
     
# import seaborn as sns


# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set(style="darkgrid")

# days_df = sns.load_dataset("express way traffic by day")
# g = sns.FacetGrid(days_df, row="cars", col="day of week", margin_titles=True)
# bins = np.linspace(0, 60, 13)
# g.map(plt.hist, "cars per day of week", color="steelblue", bins=bins, lw=0)
