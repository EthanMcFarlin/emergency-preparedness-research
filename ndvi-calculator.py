# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:31:55 2019
@author: Iris Xia
goal: try using numpy arrays to calculate and get the ndvi calculation
"""

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from osgeo import gdal
import os
import processing
import numpy
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *


#import data 
bastrop_files = r"C:/Users/irisx/Documents/SEES 2019/Bastrop Files"

#create directory for output files
output = r"C:/Users/irisx/Documents/SEES 2019/Output Files"

try: 
    os.mkdir(output)
except FileExistsError:
    print("file made")

#create dictionary for different instruments 
ndvi_bands = {
        'LT05' : ['SRB3', 'SRB4'],
        'LE07' : ['SRB3', 'SRB4'],
        'LC08' : ['SRB4', 'SRB5']
}
#create for loop to run through all dates in time series - will do when get more data
for date in os.listdir(bastrop_files):
    
    #get the satellite used for that day
    if ('LT05' in date):
        satellite = 'LT05'
    elif ('LE07' in date):
        satellite = 'LE07'
    elif ('LC08' in date):
        satellite = 'LC08'
    
    #change working directory to that file
    day = bastrop_files + '/' + date

    #for each date, loop through layers to get red and nir
    for band in os.listdir(day):
        
        if (band.endswith('tif')):
            
            #create band path to open file
            band_path = day + '/' + band
    
            #assign bands for nir and red
            if (ndvi_bands[satellite][0] in band):
                red = gdal.Open(band_path)
                redband = red.GetRasterBand(1)
            elif (ndvi_bands[satellite][1] in band):
                nir = gdal.Open(band_path)
                nirband = nir.GetRasterBand(1)
    
    #make output path for this date
    output_path = output + "/" + date + '.tif'
    
    redarr = BandReadAsArray(redband)
    nirarr = BandReadAsArray(nirband)
    
    #calculation
    ndvi = ((nirarr - redarr)/(nirarr + redarr)) * 1000
    
    #driver for out file
    driver = gdal.GetDriverByName("GTiff")
    output_driver = driver.Create(output_path, red.RasterXSize, red.RasterYSize, 1, redband.DataType)
    CopyDatasetInfo(red, output_driver)
    output_band = output_driver.GetRasterBand(1)
    output_band.WriteArray(ndvi)





