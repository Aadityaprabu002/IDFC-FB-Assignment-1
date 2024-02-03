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
        total_sum = 0
        for card in cards:
            c = card.split(':')[1].strip().split('|')
            left =  set(map(self.__convert,c[0].strip().split()))
            right = list(map(self.__convert,c[1].strip().split()))
            score = 0
            for r in right:
                if r in left:
                    if score == 0:
                        score = 1
                    else: 
                        score*=2
            total_sum += score
        
        self.__output = str(total_sum)

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

