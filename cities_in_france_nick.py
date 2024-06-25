from pyqgis_scripting_ext.core import *

#cleanup
HMap.remove_layers_by_name(["OpenStreetMap"]) #because when you run this below, without this cleanup, it will keep adding the layers so in this case it only keeps one
folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS"
geopackagePath = folder + "/vector_geopackage/packages/natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"

#load openstreetmap tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

#load the countries layer
citiesLayer = HVectorLayer.open(geopackagePath, citiesName)
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

print("Schema (first 4 fields):")
counter = 0 
for name, type in countriesLayer.fields.items():
    counter += 1 
    if counter < 5:
        print("\t", name, "of type", type)
        
crs = countriesLayer.prjcode
print("Projection:", crs)
print("Spatial extent:", countriesLayer.bbox())
print("Feature count:", countriesLayer.size())


print("Attributes for France:")
nameIndex = countriesLayer.field_index("NAME")
countriesFeatures = countriesLayer.features()
for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name == "France":
        geometryFrance = feature.geometry
        print("Geom:", geometryFrance.asWkt()[:50] +"...")
        break 

CitiesnameIndex = citiesLayer.field_index("NAME")
citiesFeatures = citiesLayer.features()
for feature in citiesFeatures:
    citygeometry = feature.geometry
    if geometryFrance.intersects(citygeometry):
        cityName = feature.attributes[CitiesnameIndex]
        print(cityName)
        

        
        