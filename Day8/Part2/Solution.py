from pprint import pprint
from math import lcm
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
        data = self.__input.split('\n')
        steps = data.pop(0)
        data.pop(0)
        graph = dict()
        for row in data:
            f = row[0:3]
            l = row[7:10]
            r = row[12:15]
            graph[f] = [l,r]
       
        start = []
        for node in graph.keys():
            if node[-1] == 'A':
                start.append(node)
        
        print(start)
        first_z_hit = [] 
        for node in start:
            cur = node
            sc = 0
            flag = False
            while not flag:
                for step in steps:
                    sc+=1
                    next = int(step == 'R')
                    cur = graph[cur][next]
                    if cur[-1] == 'Z':
                        flag = True
                        break
            first_z_hit.append(sc)


        first_z_hit = set(first_z_hit)
        
        self.__output = str(lcm(*first_z_hit))
   

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

