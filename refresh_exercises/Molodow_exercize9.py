folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/data"

csvPath = f"{folder}/01_exe9_data.csv"

with open(csvPath, "r") as file:
    result = file.readlines()
    print(result)
    
#Now I just need to print only the numbers 

    for item in result:
        if item[0].isdigit():
            print(item)

