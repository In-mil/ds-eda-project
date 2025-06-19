# %%
#import libs

import warnings

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


from matplotlib.ticker import PercentFormatter
plt.rcParams.update({ "figure.figsize" : (8, 5),"axes.facecolor" : "white", "axes.edgecolor":  "black"})
plt.rcParams["figure.facecolor"]= "w"
pd.plotting.register_matplotlib_converters()
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# %%
#import the data to a pandas dataframe
df = pd.read_csv('/Users/ina/Documents/spicedAcademy/ds-eda-project/data/20250618_King_county_house_sales_ks_JOIN.csv')

# %%
# Examine the usual suspects: head, tail, unique values etc. 
df.shape # len(df) gives the same
df.head()
df.tail()
df.columns
df.nunique() #df['colimn'].nunique() # gives you the number / df['column'].unique() # gives values
df.info()
df.describe()
df.isna().sum() # same as df.isnull().sum()
df.dtypes
df.duplicated()


# %%
#date was an object -> converted to datetime (datetime64[ns])
df['date'] = pd.to_datetime(df['date'])

# %%
#check if column was converted succesfully to datetime
df.info()

# %%
#check Nans
df.isna().sum()
#waterfront       2391
#view               63
#sqft_basement     452
#yr_renovated     3848

# %%
#fill nans wirh 0, so like no waterfront
#so basically since all the nans were in categorical columns, I filled those with "0", which is defined as "NO"
df.fillna({  
    'waterfront': 0,
    'view': 0,
    'sqft_basement': 0,
    'yr_renovated': 0
}, inplace=True) #overring

# %%
#check filling nans
df.isna().sum()


# %%
df.dtypes

# %% [markdown]
# house_id                  int64 | price                  float64
# id                        int64 |bedrooms                float64
# id.1                      int64 |bathrooms               float64
# grade                     int64 |sqft_living             float64
# condition                 int64 |sqft_lot                float64
#                                 |sqft_above              float64
#                                 |sqft_basement           float64
#                                 |yr_built                  int64
#                                 |yr_renovated            float64
#                                 |zipcode                   int64
#                                 |lat                     float64
#                                 |long                    float64
#                                 |sqft_living15           float64
#                                 |sqft_lot15              float64
# 

# %%
#Examine the descriptive statistics of the dataset.
df.describe()

# %%
#analyze price
df['price'].describe()

# %%
#prices comparison regarding zip/locations

sns.boxplot(data=df, x='zipcode', y='price')
plt.yscale('log')  # Set y-axis to log scale
plt.show()

# %%


# %%


# %%


# %%
#save; do not forget .csv within file name
df.to_csv('df1_understanding_the_data.csv',index=False)


