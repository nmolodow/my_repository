folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/programming_refresh/"



csvPath = f"{folder}stations.txt"
with open(csvPath, "r") as file:
    lines = file.readlines() 
print(lines[:19])