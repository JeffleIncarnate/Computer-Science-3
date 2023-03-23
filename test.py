list1 = [1, 2, 3, 4]
list3 = [100, 200, 300, 400]

for i, value in enumerate(list1):
    print(value, list3[int(f"-{i + 1}")])
