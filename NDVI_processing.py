"""
Created on Sat July 20th
@author: Iris Xia
Goal: output statistics for NDVI layers, output csv file of NDVI mean over time
"""
from qgis.core import QgsRasterBandStats

#loop through NDVI files in the directory to do this stuff
stats = layer.dataProvider().bandStatistics(1, QgsRasterBandStats.All)

#write string lines that show the different stats
min_value = "Minimum Value: " + str(stats.minimumValue)
max_value = "Maximum Value: " + str(stats.maximumValue)
mean = "Mean: " + str(stats.mean)
range = "Range: " + str(stats.range)
st_dev = "Standard Deviation: " + str(stats.stdDev)
sum = "Sum: " + str(stats.sum)

#make list of all stats
all_stats = [min_value, max_value, mean, range, st_dev, sum]

#create text file for output and write stats to that file
with open("C:/Users/irisx/Documents/SEES 2019/Output Files/LC08_CU_016016_20130808_20190506_C01_V01_SR_stats.txt", "w") as stat_file:
    for line in all_stats:
        stat_file.write(line)
        stat_file.write("\n")
    stat_file.close()               