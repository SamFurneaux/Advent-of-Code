import numpy as np
with open("day_2_input.txt") as file:
    ids = file.read().strip() 

ids = [id for id in ids.split(',') if id]


test = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224','1698522-1698528','446443-446449','38593856-38593862','565653-565659','824824821-824824827','2121212118-2121212124']


def import_range(num_range_str):
    min,max = num_range_str.split('-')
    min = int(min)
    max = int(max)
    return min, max

def num_check(min, max, num_list):
    for value in range(min, max + 1):
        total_len = len(str(value))
        if total_len % 2 != 0:
            continue
        num = str(value)
        if num[:int(len(num)/2)] == num[int(len(num)/2):]:
            num_list.append(int(num))
    return num_list
    
def main(range_list):
    num_list=[]
    for i in range_list:
        min, max = import_range(i)
        num_list = num_check(min,max, num_list)
    print(sum(num_list))
        


main(ids)