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
        
        #assign bands for nir and red
        if (ndvi_bands[satellite][0] in band):
            red = gdal.Open(band)
            redband = red.GetRasterBand(1)
        elif (ndvi_bands[satellite][1] in band):
            nir = gdal.Open(band)
            nirband = nir.GetRasterBand(1)
          
    #make entries list for raster calculator
    entries = []
    
    #make output path for this date
    output_path = output + "/" + date
        
    # Define red entry
    red1 = QgsRasterCalculatorEntry()
    red1.ref = 'band@3'
    red1.raster = redband
    red1.bandNumber = 3
    entries.append(red)
    
    # Define nir entry
    nir1 = QgsRasterCalculatorEntry()
    nir1.ref = 'band@4'
    nir1.raster = nirband
    nir.bandNumber = 4
    entries.append(nir)
    
    ###layer = hypothetical raster layer that needs to be made from the dataset and bands from gdal
    
    # perform calculation
    calc = QgsRasterCalculator( '((band@4 - band@3)/(band@4 + band@3)) * 1000', output_path, 'GTiff', layer.extent(), layer.width(), layer.height(), entries )
    calc.processCalculation()
    
    #add raster layer to qgis
    iface.addRasterLayer(output_path, layer)
    
    ##need to output statistics file as well
    
    







