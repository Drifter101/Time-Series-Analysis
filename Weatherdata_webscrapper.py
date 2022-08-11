# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:58:30 2022

@author: Nicol
"""

# Climate data scrapper 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import matplotlib
import pmdarima as pm
import meteostat

from datetime import datetime
from meteostat import Point, Daily, Monthly, Normals, Hourly
from meteostat import Stations
from tqdm import tqdm_notebook
import itertools
from itertools import product
import warnings
warnings.filterwarnings('ignore')


# Set time period
start = datetime(1970, 1, 1)
end = datetime(2021, 12, 30)

#Use longitud and latitud for finding nearby stations
stations = Stations()
stations = stations.nearby(48.87340095547229, 2.357350985989415)
stations = stations.fetch(5)
print(stations)

#Use the station code for downloading the data

df = Monthly("07149", start,end)
df = df.normalize()
df = df.aggregate("1Y")
df = df.fetch()

# Plot line chart including average, minimum and maximum temperature
df.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()


# Other useful commands
#Setting a month column and removing empty columns
df2 = df
df2 = df2.drop(df2.columns[[4, 5, 6]], axis= 1)
df2 = df2.dropna()
df2['month'] = pd.DatetimeIndex(df2.index).month
df2.iloc[[0,-1]]

#Check for missing values
df2[['prcp', 'tavg', 'tmax', 'tmin']].isna().sum()



















