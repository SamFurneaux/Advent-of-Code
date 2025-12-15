import numpy as np
with open("day_2_input.txt") as file:
    ids = file.read().strip() 

ids = [id for id in ids.split(',') if id]

def num_check_3(min, max, num_list):
    for value in range(min, max + 1):
        s = str(value)
        n=0
        while n <= (len(s)/2):
            if n ==0:
                if all(val == list(s)[0] for val in s):
                    if len(s) >1:
                        n = len(s)
                        num_list.append(int(s))
                n+=1
            elif (len(s)/n) == int(len(s)/n):
                if len(list(s)[0:n]) <=1:
                    n +=1
                else:
                    num_split = [s[i:i+n] for i in range(0, len(s), n)]
                    if all(val == num_split[0] for val in num_split):
                        n = len(s)
                        num_list.append(int(s))
                    n+=1
            else:
                n+=1
    return num_list

def import_range(num_range_str):
    min,max = num_range_str.split('-')
    min = int(min)
    max = int(max)
    return min, max

def main(range_list):
    num_list=[]
    for i in range_list:
        min, max = import_range(i)
        num_list = num_check_3(min,max, num_list)
    print(sum(num_list))

main(ids)