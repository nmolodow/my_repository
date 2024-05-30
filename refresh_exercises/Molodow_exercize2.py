#exercize2 
folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data"


csvPath = f"{folder}/01_exe2_data.csv"

with open(csvPath, 'r') as file:
    lines = file.readlines()
   
for line in lines:
    line = line.strip()
    lineSplit = line.split(";")
    print(lineSplit)
    
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    print(analogSplit)
    x1 = float(analogSplit[1])
    
    
    
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])
    #print(x1, y2)
    
    maxanalogString = lineSplit[2]
    maxanalogSplit = maxanalogString.split(":")
    x2 = float(maxanalogSplit[1])
    print(x1, x2, y2)
    
    y1 = y2 * x1/x2

    print(x1, x2, y1, y2)

