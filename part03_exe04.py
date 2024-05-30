from pyqgis_scripting_ext.core import *

folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/"
filePath = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data/stations.txt"

HMap.remove_layers_by_name(["OpenStreetMap", "stations", "centroids", "ne_50m_admin_0_countries"])

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

geopackagePath = f"{folder}vector_geopackage/packages/natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"


countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

ranges = [
    [80000000, float('inf')], # this is 80million up to infinity
    [1000000, 80000000],
    [float('-inf'), 1000000],
]

styles = [ #the below makes it transparent, so you can still see the osm underneath
    HFill("255, 0, 0, 70"), #only red, overlaying with transparency
    HFill("0, 255, 0, 70"), #only green
    HFill("0, 0, 255, 70")  #only blue
] #the numbers are 255 is the max value of that color, so 70 is only 70 out of 255 transparency

labelStyle = HLabel("POP_EST") + HHalo()

countriesLayer.set_graduated_style("POP_EST", ranges, styles, labelStyle)

HMap.add_layer(countriesLayer)





