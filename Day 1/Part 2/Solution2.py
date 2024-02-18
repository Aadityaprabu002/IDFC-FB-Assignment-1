from pprint import pprint
import re
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
        numbers = [ 'one', 'two' ,'three', 'four' ,'five' ,'six', 'seven' ,'eight' ,'nine']
        regex = "(?=(" + "|".join(numbers) +"|\\d))"
        words = self.__input.split('\n')
        tot = 0
        for word in words:
            res = re.findall(regex,word)
            first = res[0]
            last = res[-1]
            if first in numbers:
                first = str(numbers.index(first)+1)
            if last in numbers:
                last = str(numbers.index(last)+1)
            
            first += last
            print(first)
            tot += int(first)
       
        self.__output += str(tot)


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

