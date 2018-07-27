# netCDFclip2DEM
Author: Perry I. Houser
Contact: pihouser@gmail.com
Date: July 2018

QGIS Python code for importing FLDAS netCDF rainfall file clipped to a South Sudan basin area DEM.
Code is meant to run outside/free of QGIS, calls QGIS3 functions via python3 bindings from the terminal/command line, looped to be able to run a series of clipping FLDAS files to the DEM.
Developed on: Mac OS X 10.13 High Sierra using: QGIS3, Python3, GDAL2, OSGEO4W, QTpy5
Data Source: NASA FLDAS EA01 (East Africa 01) saved as a netCDF file
             South Sudan Digital Elevation Model (DEM) provided by ISI-USC. 
Code Status: NOT WORKING -  crashes on last line, may be due to missing PATH for the QT libraries?
Additional Notes: Will be using a linux box instead (Ubuntu 14 or 16) and python3/qgis3 advanced install
