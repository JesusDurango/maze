from os import system,name 
from readchar import key,readkey 

def maze(maze_string):
    maze_lines = maze_string.strip().split('\n')
    maze_matrix = [list(line) for line in maze_lines]
        
    return maze_matrix
    
maze_string = """
..###################
....#.....#.........#
#.#.###.#.#####.#.#.#
#.#.#...#.#.#...#.#.#
#.###.#####.#.#######
#.#...#.#...#...#.#.#
#.#.#.#.###.#.#.#.#.#
#...#.........#.....#
#.#########.#.#.###.#
#.#.#.....#.#.#.#...#
#.#.#####.#.#####.#.#
#.......#.#.#.#.#.#.#
#.#.#.#.#.###.#.###.#
#.#.#.#.#.#...#.....#
#.###.###.#.###.#####
#.#.#...#...#.#...#.#
#.#.#####.#.#.###.#.#
#...#...#.#...#...#.#
#.#.###.#####.#.#.#.#
#.#.#...........#...#
###################..
"""


def update_screen(maze):
    system('cls' if name == 'nt' else 'clear')
    for row in maze:
        print(''.join(row))
    
    
def main_loop(maze_matrix, start_coords, end_coords):
    py, px = start_coords
    
    
    while (py,px) != end_coords: 
        maze_matrix[py][px]= 'P'
        update_screen(maze_matrix)
        while True:
            
            character =  readkey()
            if character == key.UP:
                if (py-1) in range (0, len(maze_matrix)):
                    if maze_matrix[py-1][px] == '.':
                        maze_matrix[py][px] = '.'
                        py -= 1
                        maze_matrix[py][px] = 'P'
                        break
            if character == key.DOWN:
                if (py+1) in range (0, len(maze_matrix)):
                    if maze_matrix[py+1][px] == '.':
                        maze_matrix[py][px] = '.'
                        py += 1
                        maze_matrix[py][px] = 'P'
                        break
            if character == key.LEFT:
                if (px-1) in range (0, len(maze_matrix[0])):
                    if maze_matrix[py][px-1] == '.':
                        maze_matrix[py][px]= '.'
                        px -= 1
                        maze_matrix[py][px] = 'P'
                        break
            if character == key.RIGHT:
                if px+1 in range (0, len( maze_matrix[0])):
                    if maze_matrix [py][px+1] == '.':
                        maze_matrix[py][px] = '.'
                        px += 1
                        maze_matrix[py][px] ='P'
                        break
 
                       
        
start_coords = (0,0)
end_coords = (20,20)

maze_matrix = maze(maze_string)

main_loop(maze_matrix, start_coords, end_coords)
