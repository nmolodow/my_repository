

def fileSummary(path, idFieldName, avgFieldName):
    with open(path, 'r') as file:
        lines = file.readlines()
        
    idIndex = None
    analyzeIndex = None
    hSum = 0 #name it hSum because you don't want to override the actual sum function
    count = 0
    uniqueIdsList = []
    for line in lines[:10]:
        line = line.strip() #removes white spaces
        if line.startswith("#"): #so we can get the header
            fields = line.strip("#").split(",")
            
            for index, field in enumerate(fields): #enumerate also gives you an index, where one is the position
                field = field.strip()
                if field == idFieldName:
                    idIndex = index
                elif field == avgFieldName:
                    analyzeIndex = index
        else:
            #Here data starts
            lineSplit = line.split(",")
            value = float(lineSplit[analyzeIndex])
            if value != -9999:
                hSum += value 
                count += 1 
                
            idValue = lineSplit[idIndex]
            if idValue not in uniqueIdsList:
                uniqueIdsList.append(idValue)
            
            

    avg = hSum/count
    print(f"File info: {path}")
    print("================")
    print(f"Distinct count of field {idFieldName}: {len(uniqueIdsList)}")
    print(f"Average value of field {avgFieldName}: {avg}")
    print("Fields:")
    for field in fields:
        print(f" -> {field.strip()}")

    




fileSummary("/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/programming_refresh/station_data.txt", "STAID", "RR")
print("*****************")
fileSummary("/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/programming_refresh/stations.txt", "CN", "HGHT")




