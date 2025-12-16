import numpy as np

with open("day_3_input.txt", "r", encoding="utf-8") as f:
    batteries = [line.strip() for line in f]


#test = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']

num_list = []
for battery in batteries:
    
    ##bat = [int(num) for num in battery]
    bat = np.array(list(map(int, battery)))
    idxs = np.argsort(-bat, kind="stable")

    ##idxs = np.argsort(bat)[::-1]
    num = []
    remainder = 12
    while remainder >0:
        for i in idxs:
            if (100-i) >= remainder:
                num.append(bat[i])
                #idxs = idxs[idxs != i]
                idxs = idxs[idxs >i]
                remainder -=1
                break
            else:
                continue
    num_list.append(int(''.join(str(x) for x in num)))

print(sum(num_list))