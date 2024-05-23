mylist = ["merano", "Bolzano", "Trento", ]

print(mylist)
print("The element starts at position 0: ", mylist[0])

mylist.append("Postdam")
print(mylist)
mylist.remove("Postdam")
print(mylist)
mylist.pop(0)
print(mylist)

mylist = ["merano", "Bolzano", "Trento", ]
doIHaveBolzano = "Bolzano" in mylist
print(doIHaveBolzano)

for item in mylist:
    print(item)
    
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

for index in range(len(colors)):
    color = colors[index]
    ratio = ratios[index]
    
    print(f"{color} -> {ratio}")
    
for i in range(10):
    if i == 5:
        break
    print(f"A) {i}")
print("-------")
for i in range(10):
    if i == 5:
        continue
    print(f"B) {i}")
print("-------")

for i in range (0, 10, 2):
    print(f"C) {i}")
    
print("-------")

for i in range (10, 0, -2):
    print(f"D) {i}")
    
mylist = ["Merano", "Bolzano", "Trento"]
print(f"My original list: {mylist}")
mylist.sort()
print(f"My sorted list: {mylist}")
mylist.sort(reverse = True)
print(f"My rev sorted list: {mylist}")



mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort()
print(f"A mixed case list, sorted: {mylist}")
mylist.sort(key = str.lower)
print(f"A mixed case list, properly sorted: {mylist}")

numlist = ["002", "01", "3", "004"]
numlist.sort()
print(numlist)

numlist = ["002", "01", "3", "004"]

def toInt(string):
    return int(string)
    
numlist.sort(key = toInt)
print(numlist)



abc = ["a", "b", "c"]
cde = ["c", "d", "e"]

newabcde = abc + cde
print(newabcde)

print(";".join(newabcde))

numlist = [1.0, 2.0, 3.5, 6, 11, 34, 12]
print(max(numlist))
print(min(numlist))
print(sum(numlist))
#calculate the avergage for the list
avg = sum(numlist)/len(numlist)
print(avg)

#using a for loop
mysum = 0
count = 0
for item in numlist:
    #mysum = mysum + item
    mysum += item
    #count = count + 1
    count += 1
avg = mysum/count
print(avg)
    

#dictionaries 
TownsProvencesMap = {
    "merano": "BZ",
    "bolzano": "BZ",
    "trento": "TN"
}
print(TownsProvencesMap)
print(TownsProvencesMap["merano"])

TownsProvencesMap["potsdam"] = "BR"
print(TownsProvencesMap)

TownsProvencesMap.pop("potsdam")
print(TownsProvencesMap)

if TownsProvencesMap.get("Merano") is None:
    print("key doesn't exist")
else:
    print("key exists")
    
print(TownsProvencesMap.get("Merano", "unkown"))


for key, value in TownsProvencesMap.items():
    print(key, "is in the province of", value)

print(TownsProvencesMap.keys())
print(TownsProvencesMap.values())

keys = list(TownsProvencesMap.keys())
keys.sort()
print(keys)
for key in keys:
    print(key, "is in the provence of", TownsProvencesMap[key])
    
    
    
#reading and writing text files
filePath = "/Users/nickmolodow/Documents/2ndsemester/Advanced_GIS/programming_refresh/practice_data.txt"
data = """# stationid, datetime, temperature 
1, 2023-01-01 00:00, 12.3
2, 2023-01-01 00:00, 11.3
3, 2023-01-01 00:00, 10.3"""

#"w" writes a new file
with open(filePath, "w") as file:
    file.write(data)
#"a" aappends data in the file you already created. \n creates a new line
with open(filePath, "a") as file:
    file.write("\n1, 2023-01-01 00:00, 9.3")
    file.write("\n2, 2023-01-01 00:00, 8.3")
    
#"r" reads the data
with open(filePath, "r") as file:
    lines = file.readlines()

print("-----------")

stationsCount = {}
for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    lineSplit = line.split(",")
    stationId = lineSplit[0]
    
    counter = stationsCount.get(stationId, 0)
    counter += 1
    stationsCount[stationId] = counter
    
    print(stationsCount)

    
    




