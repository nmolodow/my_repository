def s(): 
    print(f"-------------")
    
list=[1,2,3,4,5]

for item in list:
    print(f"Number {item}")
    
s()
mylist=[10,20,30,40,50,60,70,80,90,100]

for item in mylist:
    if item < 50:
        print(f"Number {item}")

s()
list1=[1,2,3,4,5]
list2 = ["first", "second", "third", "fourth", "fifth"]

for index in range(len(list1)):
    print(f"{list1[index]} is {list2[index]}")

s()

n = 10

for row in range(n):
    variable = f"*"
    for index in range(row):
        variable += f"*"
    print(variable)





