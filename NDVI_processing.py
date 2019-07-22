"""
Created on Sat July 20th
@author: Iris Xia
Goal: output statistics for NDVI layers, output csv file of NDVI mean over time
"""
from qgis.core import QgsRasterBandStats
import os
import csv

#import NDVI data
ndvi_files = "C:/Users/irisx/Documents/SEES 2019/Output Files/NDVI Rasters"

#create list for output csv file
ndvi_meansbydate = []

#loop through NDVI files in the directory
for ndvi in os.listdir(ndvi_files):
    
    #set string with date
    date = ndvi[:-4]
    
    #create raster layer for each
    ndvi_raster = QgsRasterLayer(ndvi_files + "/" + ndvi)
    
    #run stats for raster layer
    stats = ndvi_raster.dataProvider().bandStatistics(1, QgsRasterBandStats.All)     

    #write string lines that show the different stats
    min_value = "Minimum Value: " + str(stats.minimumValue)
    max_value = "Maximum Value: " + str(stats.maximumValue)
    mean = "Mean: " + str(stats.mean)
    ndvi_range = "Range: " + str(stats.range)
    st_dev = "Standard Deviation: " + str(stats.stdDev)
    ndvi_sum = "Sum: " + str(stats.sum)

    #make list of all stats
    all_stats = [min_value, max_value, mean, ndvi_range, st_dev, ndvi_sum]
    
    #output path for text file
    output_path = "C:/Users/irisx/Documents/SEES 2019/Output Files/NDVI Stats/" + date + "_stats.txt"

    #create text file for output and write stats to that file
    with open(output_path, "w") as stat_file:
        for line in all_stats:
            stat_file.write(line)
            stat_file.write("\n")
    
    #add mean for that date to list
    ndvi_meansbydate.append([date, mean])

#export list as a csv file
with open('C:/Users/irisx/Documents/SEES 2019/Output Files/NDVI Stats/ndvi_means.csv', 'w') as ndvi_means:
    writer = csv.writer(ndvi_means)
    writer.writerows(ndvi_meansbydate)
ndvi_means.close()
