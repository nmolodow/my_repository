from pyqgis_scripting_ext.core import *

#necessary functions

def fromLatString(latString):
    sign = latString[0] # the plus or minus sign for degrees 
    latDegrees = float(latString[0:3])
    latMinutes = float(latString[4:6])
    latSeconds = float(latString[7:9])
    lat = latDegrees + latMinutes/60 + latSeconds/3600
    if sign == "-":
        lat = lat * -1
    return lat
    
def fromLonString(lonString):
    sign = lonString[0] # the plus or minus sign for degrees 
    lonDegrees = float(lonString[0:4])
    lonMinutes = float(lonString[5:7])
    lonSeconds = float(lonString[8:10])
    lon = lonDegrees + lonMinutes/60 + lonSeconds/3600
    if sign == "-":
        lon = lon * -1
    return lon

#here the script starts
lon = 11.34999
lat = 46.49808
stationsFile = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/stations.txt"
centerPoint = HPoint(lon, lat)

with open(stationsFile, 'r') as file:
    lines = file.readlines()

minDistance = 9999
nearestStationName = "none"
nearestDistancePoint = None

for line in lines[1:]:
    line = line.strip()
    
    lineSplit = line.split(",")
    name = lineSplit[1].strip()
    latString = lineSplit[3]
    lonString = lineSplit[4]
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    # print(name, latDec, lonDec)
    point = HPoint(lonDec, latDec)
    
    distance = point.distance(centerPoint)
    if distance < minDistance:
        minDistance = distance
        nearestStationName = name
        nearestDistancePoint = point
        
print(nearestStationName, "->", nearestDistancePoint)











