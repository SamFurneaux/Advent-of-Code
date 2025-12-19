import numpy as np

#test = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
#test = [line for line in test.split()]

with open("day_5_input.txt", "r", encoding="utf-8") as f:
    inventory = f.read()
inventory = [line for line in inventory.split()]
list_of_ranges = []

for line in inventory:
    if '-' in line:
        list_of_ranges.append([int(line.split('-')[0]), int(line.split('-')[1])])


list_of_ranges = np.array(list_of_ranges)
list_of_ranges = list_of_ranges[list_of_ranges[:, 0].argsort()]


i = 0
while i < len(list_of_ranges) - 1:
    if list_of_ranges[i][1] >= list_of_ranges[i + 1][0]:
        list_of_ranges[i][1] = max(
            list_of_ranges[i][1],
            list_of_ranges[i + 1][1]
        )

        list_of_ranges = np.delete(list_of_ranges, i + 1, axis=0)


    else:
        i += 1

print(str(np.sum(list_of_ranges[:,1] - list_of_ranges[:,0]+1)))