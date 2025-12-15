import numpy as np

with open("day_3_input.txt", "r", encoding="utf-8") as f:
    batteries = [line.strip() for line in f]


test = ['811111111111119']#'987654321111111', '811111111111119' ,'234234234234278', '818181911112111']


for battery in test:
    bat = [int(num) for num in battery]
    print(np.argsort(bat))
    remainder = 100 
    #while remainder < 12:

