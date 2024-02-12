from pprint import pprint
class Solution:
    #private
    __input = ''
    __output = ''
    __board = None
    def __read_input(self):
        with open('input.txt','r') as file:
            self.__input = file.read()

        
    def __write_output(self):
        with open('output.txt','w') as file:
            file.write(self.__output)
        pass
    
    def __logic(self): 
        self.__board =  self.__input.split('\n')
        for i in range(len(self.__board)):
            self.__board[i] = list(self.__board[i])
        gr = 0
        r = len(self.__board)
        c = len(self.__board[0])

        for i in range(r):
            for j in range(c):
                if self.__board[i][j] == '*':
                    gear_pos = set()
                    for di in [-1,0,1]:
                        for dj in [-1,0,1]:
                            cur_i = i+di
                            cur_j = j+dj 
                          
                            if (cur_i < 0 or cur_i >= len(self.__board) or \
                                cur_j < 0 or cur_j >= len(self.__board[cur_i])) or \
                                not self.__board[cur_i][cur_j].isdigit():  
                                    continue
                                                       
                          
                            while cur_j > 0 and self.__board[cur_i][cur_j-1].isdigit():
                                cur_j-=1
                               
                            gear_pos.add((cur_i,cur_j))       
                                
                    if len(gear_pos) == 2:
                        nums = []
                        for x,y in gear_pos:
                           
                            ej = y
                            num = ''
                            while ej < len(self.__board[x]) and self.__board[x][ej].isdigit():
                                num += self.__board[x][ej]
                                ej += 1
                            nums.append(int(num))
                       
                        gr+= nums[0] * nums[1]

        self.__output += str(gr)

       

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

