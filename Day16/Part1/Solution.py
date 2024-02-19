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

        queue = [(0,-1,0,1)]
        seen = set()
        while len(queue) !=0 :
            x,y,dx,dy = queue.pop(0)

            x += dx
            y += dy

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue

            ch = grid[x][y]
            if ch == '.' or ( ch == '-' and dy != 0) or ( ch == '|' and dx != 0) :
                if ( x, y, dx, dy) not in seen:
                    seen.add( ( x, y, dx, dy) )
                    queue.append( ( x, y, dx, dy) )
            elif ch == '/':
                dx ,dy = -dy, -dx
                if ( x, y, dx, dy) not in seen:
                    seen.add( ( x, y, dx, dy) )
                    queue.append( ( x, y, dx, dy) )
            elif ch == '\\':
                dx ,dy = dy, dx
                if ( x, y, dx, dy) not in seen:
                    seen.add( ( x, y, dx, dy) )
                    queue.append( ( x, y, dx, dy) )
            else:
                if ch == '|':
                    for dx,dy in [(-1,0), (1,0)]:
                        if (x,y,dx,dy) not in seen:
                            seen.add((x,y,dx,dy))
                            queue.append((x,y,dx,dy))
                else:
                    for dx,dy in [(0,-1), (0,1)]:
                        if (x,y,dx,dy) not in seen:
                            seen.add((x,y,dx,dy))
                            queue.append((x,y,dx,dy))


        res = set()
        for (x,y,dx,dy) in seen:
            res.add((x,y))

        for i in grid:
            print(''.join(i))
        
        self.__output = str(len(res))   
     

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

