from pyqgis_scripting_ext.core import *


filePath = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data/stations.txt"

with open(filePath, "r") as file:
    readLines = file.readlines()

points = []
for line in readLines[1:10]: #removed the first line because it was titles
    line = line.strip()
    # print(line)
    lineSplit = line.split(",")
    statname = lineSplit[1]
    print(statname)
    lat = lineSplit[3].strip("+")
    lon = lineSplit[4].strip("+")
    latSplit = lat.split(":")
    lonSplit = lon.split(":")
    
    convLat1 = float(latSplit[1])/60
    convLon1 = float(lonSplit[1])/60
    convLat2 = float(latSplit[2])/3600
    convLon2 = float(lonSplit[2])/3600
    
    latfinal = float(latSplit[0]) + convLat1 + convLat2
    lonfinal = float(lonSplit[0]) + convLon1 + convLon2
    


    #print(lat, lon)
    #print(latSplit, lonSplit)
    # print(convLat1, convLat2, convLon1, convLon2)
    # print(latfinal, lonfinal)
    
    point = HPoint(lonfinal, latfinal)
    points.append(point)

print(points[0])


