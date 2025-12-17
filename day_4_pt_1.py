import numpy as np

with open("day_4_input.txt", "r", encoding="utf-8") as f:
    paper_rolls = f.read().replace("\n", "")
paper_rolls= np.array([x for x in paper_rolls]).reshape(int((len(paper_rolls)+1)/140),140)

#test = '..@@.@@@@.@@@.@.@.@@@@@@@.@.@@@.@@@@..@.@@.@@@@.@@.@@@@@@@.@.@.@.@.@@@@.@@@.@@@@.@@@@@@@@.@.@.@@@.@.'

#test = np.array([x for x in test]).reshape(int((len(test)+1)/10),10)

main_counter = 0
i_translations = [0,0,-1,+1,-1,+1,-1,+1]
j_translations = [-1,+1,0,0,-1,-1,+1,+1]

for i in range(140):
    for j in range(140):
        temp_count = 0
        centre = paper_rolls[i,j]
        if centre == '.':
            continue
        else:
            for x in range(8):
                if (i + i_translations[x]) <0 or (j + j_translations[x]) <0:
                    continue
                elif (i + i_translations[x]) >139 or (j + j_translations[x]) >139:
                    continue
                else:
                    if paper_rolls[(i + i_translations[x]), (j + j_translations[x]) ] == '@':
                        temp_count +=1
            if temp_count <4:
                main_counter +=1

print(main_counter)
