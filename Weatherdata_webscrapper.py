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
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
df = Monthly("07149", start,end)
df = df.normalize()
df = df.aggregate("1Y")
df = df.fetch()

# Plot line chart including average, minimum and maximum temperature
df.plot(y=['tavg', 'tmin', 'tmax'])
=======
>>>>>>> Stashed changes
pt = Monthly("07149", start,end)
pt = pt.normalize()
pt = pt.aggregate("1Y")
pt = pt.fetch()

# Plot line chart including average, minimum and maximum temperature
pt.plot(y=['tavg', 'tmin', 'tmax'])
<<<<<<< Updated upstream
=======
>>>>>>> main
>>>>>>> Stashed changes
plt.show()


# Other useful commands
#Setting a month column and removing empty columns
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
df2 = df
df2 = df2.drop(df2.columns[[4, 5, 6]], axis= 1)
df2 = df2.dropna()
df2['month'] = pd.DatetimeIndex(df2.index).month
df2.iloc[[0,-1]]

#Check for missing values
df2[['prcp', 'tavg', 'tmax', 'tmin']].isna().sum()
=======
>>>>>>> Stashed changes
pt2 = pt
pt2 = pt2.drop(pt2.columns[[4, 5, 6]], axis= 1)
pt2 = pt2.dropna()
pt2['month'] = pd.DatetimeIndex(pt2.index).month
pt2.iloc[[0,-1]]

#Check for missing values
pt2[['prcp', 'tavg', 'tmax', 'tmin']].isna().sum()
<<<<<<< Updated upstream
=======
>>>>>>> main
>>>>>>> Stashed changes


















