class Solution:
    #private
    __input = ''
    __output = ''
    def __read_input(self):
        with open('input.txt') as file:
            self.__input = file.read()

        
    def __write_output(self):
        with open('output.txt') as file:
            file.write(self.__output)
        pass
    
    def __logic(self):
        class OneStepAdvancingTrie:
            pass
        words = self.__input.split('\n')
        for word in words:

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

