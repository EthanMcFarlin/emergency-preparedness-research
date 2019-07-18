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

#import data 
bastrop_files = r"C:\Users\irisx\Documents\SEES 2019\Bastrop Files"

#create dictionary for different instruments 
nbr_bands = {
        'LT05' : ['SRB3', 'SRB4'],
        'LE07' : ['SRB3', 'SRB4'],
        'LC08' : ['SRB4', 'SRB5']
}
#create for loop to run through all dates in time series - will do when get more data
for day in os.listdir(bastrop_files):

    #for each date, loop through layers to get red and nir
    for band in os.listdir(day):
        
        #assign bands for nir and swir
        
    entries = []

# Define band1
nir = QgsRasterCalculatorEntry()
nir.ref = 'band@4'
nir.raster = layer
nir.bandNumber = 4
entries.append(nir)

# Define band2
red = QgsRasterCalculatorEntry()
red.ref = 'band@3'
red.raster = layer
red.bandNumber = 3
entries.append(red)

# Process calculation with input extent and resolution
calc = QgsRasterCalculator( '((band@4 - band@3)/(band@4 + band@3)) * 1000', path, 'GTiff', layer.extent(), layer.width(), layer.height(), entries )
calc.processCalculation()

#export the map layer as a geotiff, then open on qgis 
iface.addRasterLayer(path, output)
    
    







