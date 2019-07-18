'''INPUT VARIABLES'''

# Where to save clipped rasters
outputDir = "/Users/sean/Desktop/Clipped Data"

# coordinates
# upper left point
UX, UY =  662878 , 3340251
# lower right point
LX,  LY = 668792 , 3334140

''' SCRIPT STARTS HERE '''
import os

# get all of the loaded layers into a list
layersList =  [layer for layer in QgsProject.instance().mapLayers().values()]

# assemble the coordinates into a single string
coordinates = str(UX) + ' ' + str(UY) + ' ' + str(LX) + ' ' + str(LY)

# iterate over each layer
for layer in layersList:
    
    # assemble what will be the path and name of the output file
    outputName = outputDir + "/" + layer.name() + '_clipped.tif'
    
    # run command line gdal command
    print('gdal_translate -projwin ' + coordinates + ' -of GTiff "' + layer.source() + '" "' + outputName + '"')
    
    # print layer name into the console for debugging purposes
    print(layer.name())
    
    # load the resultant file into qgis
    qgis.utils.iface.addRasterLayer(outputName)
