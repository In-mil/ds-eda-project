# %%
#import libs (copy& pastefrom EDA file))
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
df = pd.read_csv('/Users/ina/Documents/spicedAcademy/ds-eda-project/data/df1_understanding_the_data.csv')

# %%
df.info()

# %%
df['date'] = pd.to_datetime(df['date'])
df.info()

# %%
df.isnull().sum()

# %%
#price distribution in whole King County
#df2 = df[df2['price'] < 2_500_000] #cutting outliers
price_dist_plot = sns.histplot(df['price'], bins=200, color='darkolivegreen', kde=True)
plt.title('Price Distribution in whole King County')
plt.xlabel('price in $ Mio.')
plt.ylabel('density')
#suggested by copilot
#plt.xlim(0, 5_500_000)
plt.xticks(np.arange(0, 8_500_001, 500_000), rotation=45, fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5) #grid horizontal
plt.grid(axis='y', linestyle='--', alpha=0.5) #grid vertical
plt.show(price_dist_plot)


# %%
#since the customer wanted to live in a lively and central ares; I googled what is center of population in King County. Result: Mercer Island with zipcode 98040
#I will now compare the price distribution of this area with the whole King County 
df_price_in_mercer = df[df['zipcode'] == 98040] #filtering for zipcode 98040
sns.histplot(df_price_in_mercer['price'], bins=200, color='darkorange', kde=True)
plt.title('Price Distribution in Mercer Island (Zipcode 98040)')
plt.xlabel('price in $ Mio.')
plt.ylabel('density')
#plt.xlim(0, 5_500_000)
plt.xticks(np.arange(0, 8_500_001, 500_000), rotation=45, fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5) #grid horizontal
plt.grid(axis='y', linestyle='--', alpha=0.5) #grid vertical
plt.show(price_dist_plot2)  

# %%
sns.boxplot(x=df_price_in_mercer['zipcode'], y=df_price_in_mercer['price'], color='darkorange')

plt.title('Price Distribution in Mercer Island (Zipcode 98040)')
plt.xlabel('zipcode')
plt.ylabel('price in $ Mio.')
plt.grid(axis='x', linestyle='--', alpha=0.5) #grid horizontal
plt.grid(axis='y', linestyle='--', alpha=0.5) #grid vertical
plt.show()

# %%
df_price_in_mercer['price'].describe()

'''
count       282.000
mean    1194873.638
std      607767.642
min      500000.000
25%      822000.000
50%      993750.000
75%     1387500.000
max     5300000.000'''

# %%
# Filter prices below 2,500,000 for the boxplot
filtered = df_price_in_mercer[df_price_in_mercer['price'] < 2_100_000]
sns.boxplot(x=filtered['zipcode'], y=filtered['price'], color='darkorange')

plt.title('Price Distribution in Mercer Island (Zipcode 98040)')
plt.xlabel('zipcode')
plt.ylabel('price in $ Mio.')
plt.grid(axis='x', linestyle='--', alpha=0.5) #grid horizontal
plt.grid(axis='y', linestyle='--', alpha=0.5) #grid vertical
plt.show()


# %%


# %%
#I decide to progress with the quantiles of the price distribution in Mercer Island
q1 = df_price_in_mercer['price'].quantile(0.25)
q2 = df_price_in_mercer['price'].quantile(0.50)
q3 = df_price_in_mercer['price'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}, IQR: {iqr}, Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")  

# %%
#tring to find out "midprice"
df_price_in_mercer_cleaned = df_price_in_mercer[df_price_in_mercer['price'] < 2_500_000] #cutting outliers
price_dist_plot2 = sns.histplot(df_price_in_mercer_cleaned['price'], bins=200, color='darkorange', kde=True)
plt.title('Price Distribution in Mercer Island (Zipcode 98040) without outliers')
plt.xlabel('price in $ Mio.')
plt.ylabel('density')
plt.show()

# %%
#best would be to truncate x-achsis from the right
price_dist_plot_98040 = sns.histplot(filtered_dnj1['price'], bins=100, color='darkorange', kde=True)
plt.title('Price Distribution in Mercer Island (Zipcode 98040)')
plt.xlabel('price in $ Mio.')
plt.ylabel('density')
#plt.xlim(0, 5_500_000)
plt.xticks(np.arange(0, 5_500_001, 500_000), rotation=45, fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5) #grid horizontal
plt.grid(axis='y', linestyle='--', alpha=0.5) #grid vertical
plt.show(price_dist_plot2)  

# %%
df_price_in_mercer = df[df['zipcode'] == 98040] #filtering for zipcode 98040
df_price_in_mercer_cleaned = df_price_in_mercer[df_price_in_mercer['price'] < 2_100_000] #cutting outliers
continous_vars = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors'] #histoplots of continous vars
categoric_vars = ['condition', 'grade', 'waterfront', 'view', 'zipcode'] #histoplots of categorical vars

# %%
df_price_in_mercer = df[df['zipcode'] == 98040] #filtering for zipcode 98040
df_price_in_mercer_cleaned = df_price_in_mercer[df_price_in_mercer['price'] < 2_100_000] #cutting outliers
continous_vars = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors'] #histoplots of continous vars

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 13))

for ax, column in zip(axes.flatten(), continous_vars):
    sns.histplot(x=column, data=df_price_in_mercer_cleaned, ax=ax, color='darkolivegreen', kde=True)
    ax.set_title(f'Dist. of {column} in Mercer Is', fontsize=12)
    ax.set_xlabel(column, fontsize=10)
    ax.set_ylabel('density', fontsize=10)
    ax.tick_params(axis='x', rotation=45)
    #ax.grid(axis='x', linestyle='--', alpha=0.5)
    ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()

# %%
df_price_in_mercer = df[df['zipcode'] == 98040] #filtering for zipcode 98040
df_price_in_mercer_cleaned = df_price_in_mercer[df_price_in_mercer['price'] < 2_100_000] #cutting outliers
categoric_vars = ['waterfront', 'view', 'condition', 'grade']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 12))

for ax, column in zip(axes.flatten(), categoric_vars):
    sns.countplot(x=column, data=df_price_in_mercer_cleaned, palette='magma', ax=ax) #palette magma can be found in https://matplotlib.org/cheatsheets/_images/cheatsheets-2.png
    ax.set_title(f'Count Plot of {column}')
    ax.set_xlabel(column, fontsize=10)
    ax.set_ylabel('Count', fontsize=10)
    ax.tick_params(axis='x', rotation=45)
    #ax.grid(axis='x', linestyle='--', alpha=0.5)
    ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()

# %%
df_price_in_mercer_cleaned.head()

# %%
#Preisrange von 822 000 bis 1.387.500
#Median 993.750

#how many hosue are in budgeet
houses_in_budget = df_price_in_mercer_cleaned[df_price_in_mercer_cleaned['price'].between(822000, 1387500)]

# %%
houses_in_budget.value_counts()

# %%

offer_list_nj = houses_in_budget[
    (houses_in_budget['price'].between(822000, 1387500)) &
    (houses_in_budget['grade'] >= 9) &
    (houses_in_budget['bedrooms'] >= 4) &
    (houses_in_budget['bathrooms'] >= 2) &
    (houses_in_budget['sqft_living'] >= 3000) &
    (houses_in_budget['sqft_lot'] >= 10000) &
    (houses_in_budget['floors'] >= 2) &
    (houses_in_budget['waterfront'] >= 0) &
    (houses_in_budget['view'] >= 1)]


# %%
offer_list_nj = offer_list_nj.sort_values(by='price', ascending=True)
offer_list_nj.head()

# %%
offer_list_nj.to_csv('/Users/ina/Documents/spicedAcademy/ds-eda-project/data/offer_list_nj.csv', index=False)

# %%
#avg pro zip - CHEAPEST LOCATIONS ONE MORE TIME
mean_price_per_zp = df2.groupby('zipcode')['price'].mean()

#cheapest zips
cheapest10 = mean_price_per_zp.nsmallest(10)

#plotten
plt.figure(figsize=(10, 7))
cheapest10.plot(kind='bar', color='darkolivegreen', alpha=0.5)

#visuals
    #title
plt.title('Ten most cheapest locations', fontsize=14)
    #x-label
plt.xlabel('location')
plt.xticks(rotation=45, fontsize=12)
    #y-label
plt.ylabel('AVG price in $')
plt.yticks(np.arange(0, 400_001, 50_000), fontsize=12)
plt.ylim(0, 400_000)
    #backround
#plt.gca().set_facecolor('white', alpha=0.8) #here the background color is set to white with 80% opacity
plt.grid(axis='x', linestyle='--', alpha=0.5) #grid horizontal
plt.grid(axis='y', linestyle='--', alpha=0.5) #grid vertical
plt.show()

# %%
#CONDTION INFLUNCE ON PRICE
df_price_in_mercer = df[df['zipcode'] == 98040] #filtering for zipcode 98040
df_price_in_mercer_cleaned = df_price_in_mercer[df_price_in_mercer['price'] < 2_100_000] #cutting outliers
categoric_vars = ['waterfront', 'view', 'condition', 'grade']
continous_vars = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors'] #histoplots of continous vars

sct_plot_mercer_condtion = sns.scatterplot(x='price', y='condition', data=df_price_in_mercer_cleaned, color='darkolivegreen')
plt.title('Scatter Plot of Price vs Condition in Mercer Island (Zipcode 98040)')
plt.xlabel('Price in $')
plt.ylabel('Condition')
plt.xticks(np.arange(0, 2_500_001, 250_000), rotation=45, fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5) #grid horizontal
plt.grid(axis='y', linestyle='--', alpha=0.5) #grid vertical
plt.show()

# %%
#GRADE INFLUNCE ON PRICE
reg_plot_mercer_condition = sns.regplot(x='price', y='grade', data=df_price_in_mercer_cleaned, color='darkolivegreen')
plt.title('Scatter Plot of Price vs Grade in Mercer Island (Zipcode 98040)')
plt.xlabel('Price in $')
plt.ylabel('Condition')
plt.xticks(np.arange(0, 2_500_001, 250_000), rotation=45, fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5) #grid horizontal
plt.grid(axis='y', linestyle='--', alpha=0.5) #grid vertical
plt.show()


