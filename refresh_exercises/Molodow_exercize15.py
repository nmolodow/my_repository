folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data"



csvPath = f"{folder}/stations.txt"
with open(csvPath, "r") as file:
    lines = file.readlines()
firstline = lines[0]
print(firstline)
print(len(firstline))




# stationsCount = {}
# for line in firstline:
#     firstline = line.strip()
#     if line.startswith("#") or len(line) == 0:
#         continue
#     lineSplit = line.split(",")
#     stationId = lineSplit[0]
    
#     counter = stationsCount.get(stationId, 0)
#     counter += 1
#     stationsCount[stationId] = counter
    
#     print(stationsCount)