from pprint import pprint
from time import sleep
class Solution:
    #private
    __input = ''
    __output = ''
    def __read_input(self):
        with open('input.txt','r') as file:
            self.__input = file.read()

        
    def __write_output(self):
        with open('output.txt','w') as file:
            file.write(self.__output)
        pass
    
    def __logic(self):


        
        grid = self.__input.split('\n')
       
        
        for i in range(len(grid)):
            grid[i] = list(grid[i])

        NORTH = (-1, 0)
        SOUTH = ( 1, 0)
        EAST  = ( 0, 1)
        WEST  = ( 0,-1)

        dir = {
            '|' : [NORTH ,SOUTH],
            '-' : [EAST  ,WEST],
            'F' : [SOUTH ,EAST],
            'L' : [NORTH ,EAST],
            'J' : [NORTH ,WEST],
            '7' : [SOUTH ,WEST]
        }

        sx = 0
        sy = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'S':
                    sx = i
                    sy = j
                    break
            else:
                continue
            break
        
        def border_check(i,j):
            return not (i < 0 or j < 0 or j >= len(grid[i]) or i >= len(grid))
                

        queue = []
     
        di = sx + NORTH[0]
        dj = sy + NORTH[1]
        if border_check(di,dj) and grid[di][dj] in "|F7":
            queue.append((di,dj))

        di = sx + SOUTH[0]
        dj = sy + SOUTH[1]
        if border_check(di,dj) and grid[di][dj] in "|JL":
            queue.append((di,dj))

        di = sx + EAST[0]
        dj = sy + EAST[1]
        if border_check(di,dj) and grid[di][dj] in "-7J":
            queue.append((di,dj))

        di = sx + WEST[0]
        dj = sy + WEST[1]
        if border_check(di,dj) and grid[di][dj] in "-FL":
            queue.append((di,dj))
        
        
        seen = {(sx,sy)}
        while len(queue) != 0:
            
            x,y = queue.pop(0)
            seen.add((x,y))
            ch = grid[x][y]
            next_dir = dir[ch]
            for i,j in next_dir:
                if not border_check(x+i,y+j) or (x+i,y+j) in seen or grid[x+i][y+j] == '.':
                    continue

                if (i,j) == NORTH and grid[x+i][y+j] in "|F7":
                    queue.append((x+i,y+j))
                elif (i,j) == SOUTH and grid[x+i][y+j] in "|JL":
                    queue.append((x+i,y+j))
                elif (i,j) == EAST and grid[x+i][y+j] in "-7J":
                    queue.append((x+i,y+j))
                elif (i,j) == WEST and grid[x+i][y+j] in "-FL":
                    queue.append((x+i,y+j))

        
  
        if grid[sx + 1][sy + 0] in 'L|J' and grid[sx - 1][sy + 0] in '7|F':   # NORTH SOUTH
            grid[sx][sy] = '|'
        elif grid[sx + 0][sy + 1] in '-7J' and grid[sx + 0][sy - 1] in '-FL': # EAST WEST
            grid[sx][sy] = '-'
        elif grid[sx - 1][sy + 0] in 'F|7' and grid[sx + 0][sy + 1] in '-7J': # NORTH EAST
            grid[sx][sy] = 'L'
        elif grid[sx - 1][sy + 0] in 'F|7' and grid[sx + 0][sy - 1] in '-FL': # NORTH WEST
            grid[sx][sy] = 'J'
        elif grid[sx + 1][sy + 0] in 'L|J' and grid[sx + 0][sy + 1] in '-7J': # SOUTH EAST
            grid[sx][sy] = 'F'
        elif grid[sx + 1][sy + 0] in 'L|J' and grid[sx - 1][sy + 0] in '-FL': # SOUTH WEST
            grid[sx][sy] = '7'


        
        tot = 0
        for i in range(len(grid)):

            for j in range(len(grid[i])):
                ch = grid[i][j]
                print(ch,end='')
                count = 0
                if (i,j) not in seen:
                    for k in range(j):
                        if (i,k) not in seen: continue
                        count += grid[i][k] in {'J','L','|'}
                    if count > 0:
                        if count%2 !=0:
                            tot+=1
                


        self.__output = str(tot)
    #public
    def run(self):
        self.__read_input()
        self.__logic()
        self.__write_output()

    def __init__(self):
        self.__input = ''
        self.__output = ''
        pass
    
if __name__ == '__main__':
    solution = Solution()
    solution.run()

