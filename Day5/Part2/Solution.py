import math
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
        data = self.__input.split('\n\n')
        range_maps = []
        for i in range(1,len(data)):
            range_maps.append( data[i].split(':')[1].split('\n')[1::] )
        
        seeds = data[0].split(':')[1] 
        seeds = list(map(int,seeds.split(' ')[1::]))  
        temp = []
        for i in range(0,len(seeds),2):
            temp.append((seeds[i],seeds[i]+seeds[i+1]))

        seeds = temp

        for each_range_map in range_maps:
            ranges = []
            for r in each_range_map:
                ranges.append(list(map(int,r.split(' '))))

            res = []
            while len(seeds) > 0:
                start ,end = seeds.pop()
                for dest,src,rl in ranges:
                    overlap_start = max(start,src)
                    overlap_end = min(end,src+rl)
                    if overlap_start < overlap_end:
                        res.append((overlap_start - src + dest,overlap_end - src + dest))
                        if overlap_start > start:
                            seeds.append((start, overlap_start))
                        if end > overlap_end:
                            seeds.append((overlap_end, end))
                        break
                else:
                    res.append((start,end))
            seeds = res

        self.__output = str(min(res)[0])
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

