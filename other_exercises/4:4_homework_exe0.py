from pyqgis_scripting_ext.core import *

filePath = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data/02_exe0_geometries.csv"

with open(filePath, "r") as file:
    lines = file.readlines()
# print(lines)
canvas = HMapCanvas.new()
canvas.set_extent([0,0,60,60])
canvas.show()

new_list_coords = []
for line in lines:
    line = line.strip().split(";")
    # print(line)
    if line[0] == "line": #can I also say 'and line[2] == "1":'
        coords = line[1].split(' ')
        for coord in coords:
            coord_list = coord.split(',')
            coords = [float(coord) for coord in coord_list]
            new_list_coords.append(coords)
        print(new_list_coords)
        line = HLineString.fromCoords(new_list_coords)
        canvas.add_geometry(line, "red", 2)
    elif line[0] == "polygon":
        coords = line[1].split(' ')
        for coord in coords:
            coord_list = coord.split(',')
            coords = [float(coord) for coord in coord_list]
            new_list_coords.append(coords)
        print(new_list_coords)
        polygon = HPolygonString.fromCoords(new_list_coords)
        canvas.add_geometry(line, "blue", 2)
    
    
    