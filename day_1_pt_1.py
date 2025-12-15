#%% Import packages and data
with open("day_1_input.txt", "r", encoding="utf-8") as f:
    rotations = [line.strip() for line in f]

#%% Code
# Function to unpack inputs
def unpack_input(txt):
    l_r = txt[0]
    num = int(txt[1:]) 
    if l_r == 'L':
        num = num * -1
    return num, l_r

# Case if right rotation
def r_case(num, rot, counter):
    while rot > 0:
        if (num + rot) > 99:
            rot = rot -(100 - num)
            num = 0        
        else:
            num = num+rot
            rot = 0
    return num, counter

# Case if left rotation
def l_case(num, rot, counter):
    while rot < 0 :
        if (num+rot) < 0 :
            rot = rot - (-1-num)
            num = 99
        else:
            num = num +rot
            rot = 0
    return num, counter

# Main function
def main(list):
    start = 50
    counter = 0
    current_num = start
    for input in list:
        rotation, l_r = unpack_input(input)
        if l_r == 'L':
            current_num, counter = l_case(current_num, rotation, counter)
        elif l_r == 'R':
            current_num, counter = r_case(current_num, rotation, counter)
        if current_num == 0:
            counter +=1
    return counter

#%% Testing
test = ['L68', 'L30','R48','L5','R60','L55','L1','L99','R14','L82']

print(main(rotations))
