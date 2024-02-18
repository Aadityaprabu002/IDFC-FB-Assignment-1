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
        report = []
        for line in self.__input.split('\n'):
            report.append([list(map(int,line.split(' ')))])
        

        def difference(arr):
            return [arr[i+1] - arr[i] for i in range(len(arr)-1)]


        def add_zero_back(arr):
            while not all([x == 0 for x in arr[-1]]):
                arr.append(difference(arr[-1]))
                
            arr[-1].append(0)
            for i in range(len(arr)-2,-1,-1):
                arr[i].append(arr[i][-1] + arr[i+1][-1])
            
            return arr[0][-1]

        tot = 0
        for i in range(len(report)):
            tot += add_zero_back(report[i])

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

