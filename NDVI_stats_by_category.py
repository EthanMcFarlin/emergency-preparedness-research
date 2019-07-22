'''
Created on 21 July 2019

@author: Sean Yang

Goal: To output the statistics of each NDVI layer, clipped by burn severity, of each day. Each burn severity of each day will output its own text file while a CSV file will be outputted for the mean of every burn severity of every day to assist in time series analysis.
'''

'''SCRIPT STARTS HERE'''
'''
version 1

# Input and output directories
inputDir = "/Users/sean/Desktop/QGIS Files/NDVI_clipped_to_dNBR_categories"
outputDir = "/Users/sean/Desktop/QGIS Files/NDVI_categorized_stats"

# Loop through the folders of the input directory
inputFolders = os.listdir(inputDir)

for day in inputFolders:
    
    # for each day (which is a subfolder inside the inputDir), loop through each NDVI layer, categorized by burn severity
    NDVICategorizedLayers = os.listdir(inputDir + "/" + day)
    
    for NDVICategoryLayer in NDVICategorizedLayers:
        
        # Concatenate file path
        filePath = inputDir + "/" + day + "/" + NDVICategoryLayer
        # Load the layer (file path and layer name)
        layer = QgsRasterLayer(filePath, NDVICategoryLayer)
        # Add the layer to the qgis map
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        
        #create raster layer
        ndvi_raster = QgsRasterLayer(ndvi_files + "/" + ndvi)
        
        # get the statistics of this layer
        stats = layer.dataProvider().bandStatistics(1, QgsRasterBandStats.All)
        
        #write string lines that show the different stats
        NDVI_min_value = "Minimum Value: " + str(stats.minimumValue)
        NDVI_max_value = "Maximum Value: " + str(stats.maximumValue)
        NDVI_mean = "Mean: " + str(stats.mean)
        NDVI_range = "Range: " + str(stats.range)
        NDVI_st_dev = "Standard Deviation: " + str(stats.stdDev)
        NDVI_sum = "Sum: " + str(stats.sum)
'''
        
        




"""
version 2

Created on Sat July 20th
@author: Sean Yang & Iris Xia
Goal: output statistics for NDVI layers, categorized by burn severity, output csv file of NDVI mean over time for each category.
"""
from qgis.core import QgsRasterBandStats
import os
import csv

#import NDVI data
ndvi_files = "/Users/sean/Desktop/QGIS Files/NDVI_clipped_to_dNBR_categories"

#create list for output csv file
ndvi_meansbydate = []

#loop through each date folder in the directory
for dateFolder in os.listdir(ndvi_files):
    
    # skip hidden folders
    if dateFolder.startswith('.'):
        continue
    
    # set string with date
    date = dateFolder[15:23]
    
    #create the output directory for each date
    outputDir = "/Users/sean/Desktop/QGIS Files/NDVI_stats_by_category"
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)
    
    #for each ndvi burn severity file in each date folder
    for ndvi in os.listdir(ndvi_files + "/" + dateFolder):
        
        # skip hidden folders and files that aren't .tif
        if ndvi.startswith('.') or not ndvi.endswith('.tif'):
            continue
        
        # set string with burn severity category
        indexStartOfCategory = ndvi.index("SR") + 3
        indexEndOfCategory = -4
        category = ndvi[indexStartOfCategory:indexEndOfCategory]

        #create raster layer for each
        ndvi_raster = QgsRasterLayer(ndvi_files + "/" + dateFolder + "/" + ndvi)
        print(ndvi_files + "/" + dateFolder + "/" + ndvi)

        #run stats for raster layer
        stats = ndvi_raster.dataProvider().bandStatistics(1, QgsRasterBandStats.All)     

        #write string lines that show the different stats
        min_value = "Minimum Value: " + str(stats.minimumValue)
        max_value = "Maximum Value: " + str(stats.maximumValue)
        mean_value = str(stats.mean)
        mean_string = "Mean: " + mean_value
        ndvi_range = "Range: " + str(stats.range)
        st_dev = "Standard Deviation: " + str(stats.stdDev)
        ndvi_sum = "Sum: " + str(stats.sum)

        #make list of all stats
        all_stats = [min_value, max_value, mean, ndvi_range, st_dev, ndvi_sum]

        #output path for text file
        output_path = "/Users/sean/Desktop/QGIS Files/NDVI_stats_by_category/" + date + "_stats.txt"

        #create text file for output and write stats to that file
        with open(output_path, "w") as stat_file:
            for line in all_stats:
                stat_file.write(line)
                stat_file.write("\n")

        #add mean for that date to list
        ndvi_meansbydate.append([date, category, mean_value])

#export list as a csv file
with open('/Users/sean/Desktop/QGIS Files/NDVI_stats_by_category/NDVI_means_by_category.csv', 'w') as ndvi_means:
    writer = csv.writer(ndvi_means)
    writer.writerows(ndvi_meansbydate)
ndvi_means.close()       
