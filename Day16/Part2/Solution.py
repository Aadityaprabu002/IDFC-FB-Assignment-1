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
        
        def get_tiles(x,y,dx,dy):

            queue = [(x,y,dx,dy)]
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
            return len(res)
            
        mx = 0

        for r in range(len(grid)):
            mx = max(mx, get_tiles(r, -1, 0, 1))
            mx = max(mx, get_tiles(r, len(grid[0]), 0, -1))
            
        for c in range(len(grid)):
            mx = max(mx, get_tiles(-1, c, 1, 0))
            mx = max(mx, get_tiles(len(grid), c, -1, 0))

        self.__output = str(mx)
     

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

