from pyqgis_scripting_ext.core import *

folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/"
filePath = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data/stations.txt"

HMap.remove_layers_by_name(["OpenStreetMap", "stations"])

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

#create a schema, which dfines what we want in this new layer. 
#Defining the field and the type in the attribute table
schema = {
    "statid": "Integer",
    "statname":"string",
    "cn": "string",
    "lat": "Float",
    "lon": "Float",
    "hght": "double"
}

stationsLayer = HVectorLayer.new("stations", "Point", "EPSG:4326", schema)

with open(filePath, "r") as file:
    readLines = file.readlines()

for line in readLines[1:]: #removed the first line because it was titles
    line = line.strip()
    lineSplit = line.split(",")
    statname = lineSplit[1]
    statid = lineSplit[0]
    cn = lineSplit[2]
    hght = lineSplit[5]
    # print(statname)
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
    
    point = HPoint(lonfinal, latfinal) #xy, not yx
    attributes = [
        statid, 
        statname,
        cn,
        latfinal,
        lonfinal,
        hght
    ]
    stationsLayer.add_feature(point, attributes)

newPath = folder + "stations.gpkg" #we are creating a new path to save 

error = stationsLayer.dump_to_gpkg(newPath, overwrite=True)
if error: 
    print(error)

new_stationsLayer = HVectorLayer.open(newPath, "stations")
HMap.add_layer(new_stationsLayer)


