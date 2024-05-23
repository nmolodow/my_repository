folder = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/programming_refresh/"


csvPath = f"{folder}01_exe11_data.csv"

with open(csvPath, "r") as file:
    lines = file.readlines()
    print(lines)


for line in lines:
    line = line.strip()
    lineSplit = line.split(";")
    # print(lineSplit)
    linesplitbase = lineSplit[0].split("=")
    # print(linesplitbase)
    linesplitheight = lineSplit[1].split("=")
    # print(linesplitheight)
    linesplitbasenum = linesplitbase[1].split("cm")
    # print(linesplitbasenum)
    basenumber = float(linesplitbasenum[0])
    # print(basenumber)
    heightnumber = float(linesplitheight[1])*100
    # print(heightnumber)
    print(f"base * height / 2 = {basenumber} * {heightnumber}/2 = {basenumber*heightnumber/2}cm2")
    
    
# for line in lines:
#     for i in line:
#         if i.isdigit() == True:
#             solution = (([0]*[1])/2)
# print(solution)

#stuck here for about an hour
    
    