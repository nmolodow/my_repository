n = 10

for row in range(n, 0, -1):
    variable = f"*"
    for index in range(row):
        variable += f"*"
    print(variable)