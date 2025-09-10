n = 20
number = (10, 20, 30, 40, 20, 56)
index = [] 
for i in range(len(number)):
    if number[i] == n:
        index.append(i)
if index:
    print(f"{n} found at indexes: {index}")
else:
    print(f"{n} not found in tuple")
