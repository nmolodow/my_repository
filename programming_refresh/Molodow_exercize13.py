list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]

from collections import Counter
list1.sort()

list2.sort()

list3.sort()

list4.sort()

print(list1)
print(list2)
print(list3)
print(list4)

solution = Counter(list1+list2+list3+list4)
print(solution)

keys = list(solution.keys())
print(keys)
values = list(solution.values())
print(values)

for item in range(len(keys)):
    print(f"count of {keys[item]} = {values[item]}")

