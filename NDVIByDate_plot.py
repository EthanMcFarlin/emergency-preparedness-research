# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:21:56 2019
@author: Iris Xia
goal: create plots using matplotlib of NDVI means over time by date
"""
import matplotlib.pyplot as plt
import pandas as pd
import datetime

#read in csv file as a dataframe
ndvi_meansbydate = pd.read_csv("ndvi_means.csv", names = ["Date", "Mean"])

#sort values in dataframe by date
ndvi_meansbydate = ndvi_meansbydate.sort_values('Date')

#turn the date values into actual datetime values
for i in ndvi_meansbydate.index:
        current_date = str(ndvi_meansbydate.at[i, "Date"])
        format_date = datetime.datetime.strptime(current_date, "%Y%m%d")
        ndvi_meansbydate.at[i, "Date"] = format_date

#plot data
plt.plot(ndvi_meansbydate["Date"], ndvi_meansbydate["Mean"], "ko") #plot points
plt.plot(ndvi_meansbydate["Date"], ndvi_meansbydate["Mean"], "k-") #plot line
plt.show()