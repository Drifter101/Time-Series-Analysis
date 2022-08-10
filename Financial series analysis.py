# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:48:08 2022

@author: Nicol
"""

# This tool enables the study of financial series after downloading the data 
#  data using the FinancialData_web tool. 

# Check the data for possible missing value. 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import missingno as mno

df = data #back up original source

df.iloc[[0,-1]] #display first and last row
df.info()       #check data types

# check for missing values using the following function
def gaps(df):
    if df.isnull().values.any():
        print("MISSING values:\n")
        mno.matrix(df)
    else:
        print("no missing values\n")
gaps(df)  

plt.figure(100, figsize=(20, 7))
sns.lineplot(x = df.index, y = "AAPL", data = df, palette="coolwarm");

# for transforming the data into percentage change
df1 = df.pct_change()
df1.iloc[[0,-1]]
# transformation requires the removal of missing values for the first row
df1 = df1.dropna()
df1.iloc[[0,-1]]

#Overview of average pct change
df1.mean().plot(kind='bar', figsize=(10, 6)) 

#Overview of the cumulative sum of percentage changes over the study period
df1.cumsum().apply(np.exp).plot(figsize=(10, 6),
                                 legend=False);
# In case one is interested in obtaning the values for a time frame one can
# use this function. In this case, it draws the last value for each year
df1.resample('1y', label='right').last().head()

# Looking at individual time series

# Look at all the tickers contained in the data set
for col in df1.columns:
    print(col)
    
# Select the ticker for analysis
sym= "HG=F"
# Create a data frame with only the prices for the ticker(s) in question
df2=pd.DataFrame(df[sym]).dropna()
df2.iloc[[0,-1]] # check start and end

window = 20

# Create new columns for analysis

df2["min"] = df2[sym].rolling(window=window).min()

df2["max"] = df2[sym].rolling(window=window).max()

df2["mean"] = df2[sym].rolling(window=window).mean()

df2["std"] = df2[sym].rolling(window=window).std()

df2["ewma"] = df2[sym].ewm(halflife=0.5, min_periods=window).mean()

#Note on ewm: The moving average is designed as such that older
# observations are given lower weights. 
#The weights fall exponentially as the data point gets older
# – hence the name exponentially weighted.

# check dataframe is complete and with no Na
df2.iloc[[0,-1]] # check start and end
df2 = df2.dropna()
df2.iloc[[0,-1]] # check start and end

# Display the ticker data along with the newly created columns
# Note that the function iloc determines the number of periods shown
ax = df2[['min', 'mean', 'max']].iloc[-300:].plot(
    figsize=(10, 6), style=['g--', 'r--', 'g--'], lw=0.8)
df2[sym].iloc[-300:].plot(ax=ax, lw=2.0);

# Moving averages are an useful tool for technical anylsis.


df2['SMA1'] = df[sym].rolling(window= 52).mean()
df2['SMA2'] = df[sym].rolling(window=104).mean()
df2.iloc[[0,-1]]
df2[[sym, 'SMA1', 'SMA2']].tail()

# display the data. In case you want the entire time frame,
# remove the iloc[] bit.
ax = df2[[sym, 'SMA1', 'SMA2']].iloc[-200:].plot(figsize=(10, 6));

# Correlation analysis

# Lets start easy, with two tickers from the original dataframe (df)
# AAPL and MSFT are good candidates. 
df3=df[["AAPL","MSFT"]]

#Check Na
df3.iloc[[0,-1]]

#Plot entire dataframe
df3.plot(subplots=True, figsize=(10, 6));
# PLot selected time frame
df3.loc["2006-12-30":'2011-12-30'].plot(secondary_y="MSFT", 
                                        figsize=(10, 6));

# Lets now look at the price variation (pct change) of the same tickers
# We use the pct_change dataframe (df1)
df4=df1[["AAPL","MSFT"]]

#Check Na
df4.iloc[[0,-1]]

#Plot entire dataframe
df4.plot(subplots=True, figsize=(10, 6));
# PLot selected time frame
df4.loc["2006-12-30":'2011-12-30'].plot(figsize=(10, 6));

# Plot distribution and scatter plot
pd.plotting.scatter_matrix(df4,
                           alpha=0.5,
                           diagonal='hist',
                           hist_kwds={'bins': 35},
                           figsize=(10, 6));

# Scatter plot with correlation line
reg = np.polyfit(df4["AAPL"], df4['MSFT'], deg=1)
ax = df4.plot(kind='scatter', x='AAPL', y='MSFT', figsize=(10, 6))
ax.plot(df4["AAPL"], np.polyval(reg, df4['AAPL']), 'r', lw=2);
df4.corr()

# We can also plot the rolling corelation over time
# with a red line for the correlation static value
ax = df4["AAPL"].rolling(window=52).corr(
        df4['MSFT']).plot(figsize=(10, 6))
ax.axhline(df4.corr().iloc[0, 1], c='r');


















