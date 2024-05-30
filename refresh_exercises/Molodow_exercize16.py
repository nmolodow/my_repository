folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data"



csvPath = f"{folder}/stations.txt"
with open(csvPath, "r") as file:
    lines = file.readlines()
firstline = lines[0]

columns = firstline.split()
print(len(columns()))

