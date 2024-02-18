from pprint import pprint
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


        def print_grid(grid):
            for row in grid:
                print(''.join(row))
            
            print('')


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

        self.__output = str(len(seen) // 2)

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

