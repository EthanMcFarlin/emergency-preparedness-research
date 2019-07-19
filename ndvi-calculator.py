"""
Created on Wednesday July 17 
@author: Iris Xia
goal: write a script to map NDVI values for Landsat data
output calculated NDVI into a raster layer
output statistics into another file

"""
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from osgeo import gdal
import os
import processing

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
        
        band_path = day + '/' + band

        #assign bands for nir and red
        if (ndvi_bands[satellite][0] in band):
            red = QgsRasterLayer(band_path)
        elif (ndvi_bands[satellite][1] in band):
            nir = QgsRasterLayer(band_path)
          
    #make output path for this date
    output_raster = output + "/" + date
    
    #parameters for calculation
    parameters = {
        'INPUT_A' : red,
        'BAND_A' : 1,
        'INPUT_B' : nir,
        'BAND_B' : 1,
        'FORMULA' : '((B - A)/(B + A)) * 1000',
        'OUTPUT' : output_raster + '.tif'}

    calc = processing.runAndLoadResults('gdal:rastercalculator', parameters)
    
    
    







