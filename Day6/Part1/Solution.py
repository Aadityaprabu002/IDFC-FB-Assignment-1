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
        data =  self.__input.split('\n')
        time = [ int(i) for i in data[0].split(':')[1].strip().split(' ') if i != '' ]
        dist = [ int(i)  for i in data[1].split(':')[1].strip().split(' ') if i != '' ]
        res = []
        for i in range(len(time)):
            t = time[i]
            d = dist[i]
            c = 0
            for j in range(t):
                if ((t-j) * j) > d:
                    c+=1
            res.append(c)
        
        m = 1
        for i in res:
            m*=i
        
        self.__output = str(m)



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

