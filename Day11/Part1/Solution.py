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
        er = []
        for i,row in enumerate(grid):
            if all(cell == '.' for cell in row):
                er.append(i)
        
        ec = []
        for i,col in enumerate(zip(*grid)):
            if all(cell == '.' for cell in col):
                ec.append(i)
        
        
        galaxies = []
        for i, row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell == '#':
                    galaxies.append((i,j))

        tot = 0
        for i, (x1,y1) in enumerate(galaxies):
            for j, (x2,y2) in enumerate(galaxies[:i]):
                for k in range(min(x1,x2),max(x1,x2)):
                    tot+= 1
                    if k in er:
                        tot += 1
                for k in range(min(y1,y2),max(y1,y2)):
                    tot+= 1
                    if k in ec:
                        tot += 1

        self.__output = str(tot)
                        



        pass

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

