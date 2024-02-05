from pprint import pprint
import math
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
    
    def __map_range(self,from_value,range_map):
        cur_value = from_value
        for r in range_map:
            r = r.split(' ')
            dest = int(r[0])
            src = int(r[1])
            rl = int(r[2])
            if src <= cur_value and cur_value <= src+rl-1:
                cur_value = (dest - src) + cur_value
                return cur_value
            
        return cur_value

    def __logic(self):
        data = self.__input.split('\n\n')
        seeds = data[0].split(':')[1] 
        ranges = []
        for i in range(1,len(data)):
            ranges.append(data[i].split(':')[1].split('\n')[1::])

        min_value = math.inf
        can_map = False
        for seed in seeds.split(' ')[1::]:
            cur = int(seed)

            for r in range(len(ranges)):    
                cur = self.__map_range(cur,ranges[r])
            min_value = min(cur,min_value)
  
        self.__output = str(min_value)
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

