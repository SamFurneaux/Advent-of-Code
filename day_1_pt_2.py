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
    return num

# Main function
def main(list):
    counter = 0
    current_num = 50
    for input in list:
        rot = unpack_input(input)
        counter += abs((current_num+rot))//100
        if ((current_num+rot) <= 0) and (current_num !=0):
            counter +=1
        current_num = (current_num+rot) % 100
    return counter

#%% Testing
test = ['L68', 'L30','R48','L5','R60','L55','L1','L99','R14','L82']

print(main(rotations))
