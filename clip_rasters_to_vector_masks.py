# -*- coding: utf-8 -*-
'''
Created on Fri Jul 20 2019

@author: Sean Yang

GOAL: Clipping a group of raster layers with a group of vector mask layers. 
Each raster layer will produce its own folder inside the initial output directory.

PROCESS:
1. Clip rasters using (already) buffered vector layers
2. Set the NoData value on the newly clipped rasters to 0
3. Output raster files

(Command line gdal command used below)
gdalwarp -of GTiff -cutline "[vector file path]" -dstnodata 0.0 "[raster file path]" "[output file path]"
'''

'''INPUT VARIABLES'''

rastersInputDir = "/Users/sean/Desktop/QGIS Files/NDVI"
vectorsInputDir = "/Users/sean/Desktop/QGIS Files/dNBR Category Vectors/Buffered Category Vectors"
outputDir = "/Users/sean/Desktop/QGIS Files/NDVI_clipped_to_dNBR_categories"

'''SCRIPT STARTS HERE'''

import os

# store the input rasters and vectors each in a list
rastersFileList = os.listdir(rastersInputDir)
vectorsFileList = os.listdir(vectorsInputDir)

# create the output directory if it doesnt exist
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

# loop through all the raster files
for rasterFile in rastersFileList:
    
    # check that the raster file is a .tif
    if not rasterFile.endswith(".tif"):
        print("Issue with " + rasterFile)
        continue
    
    # log to console
    print("Clipping: " + rasterFile)

    # for each raster file, clip it with each vector file
    for vectorFile in vectorsFileList:

        # check that the vector file is a .gpkg
        if not vectorFile.endswith(".gpkg"):
            print("-> Issue with " + vectorFile)
            continue

        # every raster file gets its own folder within the output directory, containing the multiple versions of the raster file clipped to each vector
        newFolderPathAndName = outputDir + "/" + rasterFile + "_categorized"
        if not os.path.exists(newFolderPathAndName):
            os.makedirs(newFolderPathAndName)
            
        # concatenate the full file path for the raster and vector inputs
        vectorFilePath = vectorsInputDir + "/" + vectorFile
        rasterFilePath = rastersInputDir + "/" + rasterFile

        # concatenate the formatted name for this particular clipped raster file
        rasterFileNameWithoutExtension = rasterFile.replace(".tif","")
        vectorFileBurnSeverity = vectorFile[5:-21] # removes 'dNBR' and 'buffered.gpkg' from the name
        outputFileName = rasterFileNameWithoutExtension + "_" + vectorFileBurnSeverity + ".tif"

        # run the gdal warp command with parameters to clip the raster to the vector file
        os.system('gdalwarp -of GTiff -cutline "' + vectorFilePath + '" -dstnodata 0.0 "' + rasterFilePath + '" "' + newFolderPathAndName + "/" + outputFileName + '"')
        
        # log to console
        print("-> " + vectorFileBurnSeverity)
