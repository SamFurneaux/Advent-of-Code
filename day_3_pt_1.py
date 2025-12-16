import numpy as np
with open("day_3_input.txt", "r", encoding="utf-8") as f:
    batteries = [line.strip() for line in f]

test = ['987654321111111','811111111111119','234234234234278','818181911112111']

list = 0

for battery in batteries:   
    array = np.array([int(bat) for bat in battery]).reshape(-1, 1)
    if array.argmax() == len(array)-1:
        int_1 = str(array[np.argsort(np.max(array, axis=1))[-2]].item())
        int_2 = str(array[np.argsort(np.max(array, axis=1))[-1]].item())
    else:
        int_1 = str(array[array.argmax()].item())
        int_2 = str(array[array.argmax()+1:][array[array.argmax()+1:].argmax()].item())
    list += int(int_1+int_2)

print(list)