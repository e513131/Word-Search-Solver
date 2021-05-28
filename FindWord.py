import copy

word_bank = open('wordbank.txt', "r").read().split()

table = []
table_file = open('grid.txt', "r")
count = 0

while True: 
    count += 1
    line = list(table_file.readline().strip())
    
    if not line: 
        break
    table.append(line)

result = copy.deepcopy(table)

def signum(n):
    if(n < 0): return -1
    elif(n > 0): return 1
    else: return n
 
def print_grid(grid):
    for row in grid:
        for elem in row:
            print(elem, end = '')
        print()    
def grid_to_lower(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = grid[i][j].lower()

def find_firsts(char):
    result_list = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j]==char:
                result_list.append([i, j])
    return result_list

def get_ends(coor, word):
    length = len(word)
    result_list = []
    x, y = coor[1], coor[0]
    for i in range(-1,2):               #finds neighbors
            for j in range(-1,2):       #finds neighbors
                end_x = x+i*length-1*signum(i)        #x coor of last letter
                end_y = y+j*length-1*signum(j)        #y coor of last letter

                if not(end_x<0 or end_y<0 or end_x>=len(table[0]) or end_y>=len(table) or (i==j and i==0)): #makes sure its inside table
                    result_list.append([end_y, end_x])
    return result_list
    
def find(word):
    for first in find_firsts(word[0]):  #goes thru each coor that the first letter is at    
        # print("first " + str(first))
        ends = get_ends(first, word)
        for end in ends:
            offset_x = end[1] - first[1]
            dist_x = abs(offset_x)
            offset_y = end[0] - first[0]
            dist_y = abs(offset_y)

            possible = word[0]

            for i in range(1, max(dist_x, dist_y)+1):     #goes through each letter one by one
                possible = possible + table[first[0] + signum(offset_y)*i][first[1] + signum(offset_x)*i]
                if not possible == word[0: i+1]:
                    break
            if possible==word: 
                return [first[0], first[1], dist_y, dist_x]
    return "not found"

def mark(word):
    data = find(word)
    if data == "not found": 
        print(data)
        return 

    first_y, first_x, offset_y, offset_x = data
    dist_x = abs(offset_x)
    dist_y = abs(offset_y)

    for i in range(0, max(dist_x, dist_y)+1):
        row = first_y + signum(offset_y)*i
        col = first_x + signum(offset_x)*i
        result[row][col] = result[row][col].upper()

grid_to_lower(table)
grid_to_lower(result)

for word in word_bank:
    mark(word.lower())
    
print_grid(result)
