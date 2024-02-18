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
        data = self.__input.split('\n')
        steps = data.pop(0)
        data.pop(0)
        graph = dict()
        for row in data:
            f = row[0:3]
            l = row[7:10]
            r = row[12:15]
            graph[f] = [l,r]
        pprint(graph)

        cur = 'AAA'
        sc = 0
        while cur != 'ZZZ':
            for step in steps:
                next = int(step == 'R')
                cur = graph[cur][next]
                sc+=1
                print(cur)

        self.__output = str(sc)

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

