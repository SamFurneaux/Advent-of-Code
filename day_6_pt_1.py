import numpy as np

test = '123 328  51 64\n45 64  387 23\n6 98  215 314\n*   +   *   +'

with open("day_6_input.txt", "r", encoding="utf-8") as f:
    homework = f.read()

homework = [line for line in homework.split('\n') if len(line) >0 ]   ### TEST
homework = [line.split() for line in homework]
multipliers = homework[-1]
homework = np.array(homework[:-1])
homework = homework.astype('int')
homework = homework.astype('object')

sum = 0
for i in range(len(homework[0])):
    
    if multipliers[i] == '*':

        sum += np.prod(homework[:,i])
    elif multipliers[i] == '+':

        sum += np.sum(homework[:,i])
print(sum)