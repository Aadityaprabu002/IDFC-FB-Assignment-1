from collections import defaultdict
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
        games = []
        for row in data:
            game = row.split(':')[1].strip().split(';')
            games.append(game)

        tot = 0
        for game in games:
            max_map = defaultdict(int)
            for turn in game:
                color_pairs = turn.split(',')
                for color_pair in color_pairs:
                    pair = color_pair.strip().split(' ')
                    freq = int(pair[0])
                    color = pair[1]
                    max_map[color] = max(max_map[color],freq)
            pprint(max_map)
            
            tot +=  max_map['red'] * max_map['blue'] * max_map['green']  
                        
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

