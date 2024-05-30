folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data"



csvPath = f"{folder}/stations.txt"
with open(csvPath, "r") as file:
    lines = file.readlines() 
print(lines[:19])