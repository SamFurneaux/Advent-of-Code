#test = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
#test = [line for line in test.split()]

with open("day_5_input.txt", "r", encoding="utf-8") as f:
    inventory = f.read()
inventory = [line for line in inventory.split()]

list_of_ranges = []
list_of_inputs = []
for line in inventory:
    if '-' in line:

        list_of_ranges.append([int(line.split('-')[0]), int(line.split('-')[1])])
    else:
        list_of_inputs.append(int(line))

counter = 0
for input in list_of_inputs:
    for range in list_of_ranges:
        if input >= range[0] and input<= range[1]:
            counter +=1
            break
print(counter)