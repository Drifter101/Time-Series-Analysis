# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 13:34:25 2022

@author: Nicol
"""

import pandas as pd
from meteostat import Point, Daily, Monthly, Hourly
from meteostat import Stations, Normals
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from functools import reduce
import numpy as np


chillan = "85672" #ID of weather station for the region of Chillan, Chile. 
curico = "85629"  #ID of weather station for the region of Curico, Chile.
#Please use Weatherdata_webscrapper.py for finding the ID of your desire weather station.


start = datetime(2000, 1, 1)
end = datetime(2022,11, 1)

data = Daily(curico, start=start, end=end)
data = data.normalize()
#data = data.aggregate("1D")
data = data.interpolate()

data = data.fetch()


normals = Normals(curico, 1991, 2020)
normals = normals.fetch()


# Plot line chart including average, minimum and maximum temperature
normals.plot(y=['tavg', 'tmin', 'tmax'])

data["month"]=data.index.month
data["year"]=data.index.year
data=data.reset_index().merge(normals,on='month',how='left').set_index("time")



data["over_30"]= data["tmax_x"] >= 30

data["is_consecutively_over_30"] = reduce(lambda a,b: a&b, [np.roll(data["over_30"], -i) for i in range(3)])


g = data.groupby(["year"]).sum()
df = pd.DataFrame()
df["3 day"] =g["is_consecutively_over_30"]
df["1 day"] =g["over_30"]
df["year"]= df.index.year
df = df.iloc[:-1,:]

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.barplot(x=df.index.values,y="3 day",data=df, color = "r").set(title="Number of heats wave by year")
