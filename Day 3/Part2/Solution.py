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
    
    
    def __check_inside_border_and_isdigit(self,i,j,max_row,max_col):
        if i < 0 or i > max_row or j < 0 or j > max_col:
            return False
        return self.__board[i][j].isdigit()


    def __extract_number(self,board,i,j):
        print(board[i])
        print(board[i][j])
        print('')

        r = len(board)
        c = len(board[0])
        kr = j
        kl = j+1
        num = ''
        while(True):
            if kr > c or not board[i][kr].isdigit() :
                break
            num+=board[i][kr]
            kr+=1
        while(True):
            if kl < 0 or not board[i][kl].isdigit():
                break
            num = board[i][kl] + num
            kl-=1
        if num == '':
            return 1
        return int(num)

    def __logic(self):
        self.__board =  self.__input.split('\n')
        gr = 0
        r = len(self.__board)
        c = len(self.__board[0])
        for i in range(r):
            for j in range(c):
                if self.__board[i][j] == '*':
                    mul = 1
                    gears = set()
                    if self.__check_inside_border_and_isdigit(i+1,j,r,c) : #down
                        gears.add(self.__extract_number(self.__board,i+1,j))

                    if self.__check_inside_border_and_isdigit(i-1,j,r,c)  : #up
                        gears.add(self.__extract_number(self.__board,i-1,j))
                    
                    if self.__check_inside_border_and_isdigit(i,j+1,r,c): #right
                        gears.add(self.__extract_number(self.__board,i+1,j))
                    
                    if self.__check_inside_border_and_isdigit(i,j-1,r,c) : #left
                        gears.add(self.__extract_number(self.__board,i,j-1))
                    
                    if self.__check_inside_border_and_isdigit(i+1,j+1,r,c) : #right down
                        gears.add(self.__extract_number(self.__board,i+1,j+1))
                    
                    if self.__check_inside_border_and_isdigit(i-1,j-1,r,c) : #left up
                        gears.add(self.__extract_number(self.__board,i-1,j-1))
                    
                    if self.__check_inside_border_and_isdigit(i+1,j-1,r,c) : #left down
                        gears.add(self.__extract_number(self.__board,i+1,j-1))
                    
                    if self.__check_inside_border_and_isdigit(i-1,j+1,r,c): #right up
                        gears.add(self.__extract_number(self.__board,i-1,j+1))

                    if len(gears) == 2:
                        for i in gears:
                            mul*i
                    print(gears)
                    gr+=mul

        self.__output = str(gr)



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

