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
    
    def __convert(self,c):
        if c.isdigit():
            return int(c)
        return None
        
    def __logic(self):
        cards = self.__input.split('\n')        
        count_map = {}
        for id,card in enumerate(cards):
            id += 1
            if id not in count_map:
                count_map[id] = 1

            c = card.split(':')[1].strip().split('|')
            left =  set(map(self.__convert,c[0].strip().split()))
            right = list(map(self.__convert,c[1].strip().split()))
            count = 0
            for r in right:
                if r in left:
                    count+=1

            for i in range(id+1,id+count+1):
                count_map[i] = count_map.get(i,1) + count_map[id]

        self.__output = str(sum(count_map.values()))

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

