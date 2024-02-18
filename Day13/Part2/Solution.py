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
        
        def find_reflection_pointer(grid):
            for r in range(1,len(grid)):
                above = grid[:r][::-1]
                below = grid[r:]

                if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
                    return r
                
            return 0

        patterns = self.__input.split('\n\n')
        tot = 0
        for pattern in patterns:
            grid = pattern.split('\n')
            
            row = find_reflection_pointer(grid)
            
            tot += row*100

            col = find_reflection_pointer(list(zip(*grid)))

            tot += col

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

