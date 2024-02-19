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
        def hash(c,h):
            h += ord(c)
            h *= 17
            h %= 256
            return h

        words = self.__input.split(',')
        tot = 0
        for word in words:
            h = 0
            for char in word:
                h = hash(char,h)
            tot+=h
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

