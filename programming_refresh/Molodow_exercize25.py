numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]

# I need to do a for loop and iterate through and remove all of the odd numbers first
# In the loop, I need to write an if statement and remove all numbers that are not even

numbersnew = []

for number in numbers:
    
    if number % 2 == 0:
        numbersnew.append(number)

print(numbersnew)




