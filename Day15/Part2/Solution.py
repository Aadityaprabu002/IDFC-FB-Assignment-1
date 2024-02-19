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
        box = [ [] for b in range(256) ]
        box_to_fl = dict()
        for word in words:
            h = 0
            for char in word:
                h = hash(char,h)
            
            if '-' in word:
                label = word[:-1]
                index = 0
                for l in label:
                    index = hash(l,index)
                if label in box[index]:
                    box[index].remove(label)

            else:
                label , f_length = word.split('=')
                f_length = int(f_length)
                index = 0
                for l in label:
                    index = hash(l,index)
                if label not in box[index]:
                    box[index].append(label)
                box_to_fl[label] = f_length

        tot = 0
        for bno,b in enumerate(box,1):
            for lno,l in enumerate(b,1):
                tot += bno * lno * box_to_fl[l]
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

