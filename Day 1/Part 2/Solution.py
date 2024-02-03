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
        
        class Node:
            def __init__(self):
                self.children = {}
                self.is_end = False

        class OneStepAdvancingTrie:
            def __init__(self):
                self.root = Node()
                self.pointer = self.root

            def insert(self, word):
                node = self.root
                for c in word:
                    if c not in node.children:
                        node.children[c] = Node()
                    node = node.children[c]
                node.is_end = True

            def search(self, prefix):
                node = self.root
                for char in prefix:
                    if char not in node.children:
                        return False
                    node = node.children[char]
                return True
            
            def reset_pointer(self):
                self.pointer = self.root 

            def lookup_next(self, c):
          
                if c in self.pointer.children:
                    self.pointer = self.pointer.children[c] # Advance to the next position
                    if self.pointer.is_end:
                        return 1
                    return 0
                
                self.reset_pointer()
                if c in self.pointer.children:
                    self.pointer = self.pointer.children[c]
                    return -1
                return -2
    

        trie_forward = OneStepAdvancingTrie()
        trie_reverse = OneStepAdvancingTrie()
        numbers = [ 'one', 'two' ,'three', 'four' ,'five' ,'six', 'seven' ,'eight' ,'nine']
        num_map = {}
        for i in range(len( numbers )):
            num_map[numbers[i]] = i+1
        for number in numbers:
            trie_forward.insert(number)
            trie_reverse.insert(number[::-1])

        words = self.__input.split('\n')
        total_sum = 0
        for word in words:
            actual = ''
            first = 0
            for i in range(len(word)):
                if word[i].isalpha():
                    r = trie_forward.lookup_next(word[i])
                    if r == 1:
                        ans = word[first:i+1]
                        actual += str(num_map[ans])
                        break
                    elif  r == -1:
                        first = i
                    elif r == 0:
                        continue
                    elif r == -2:
                        first = i+1

                elif word[i].isdigit():
                    actual += word[i]
                    break
                    

            last = 0
            reversed_word = word[::-1]
            for i in range(len(reversed_word)):
                if reversed_word[i].isalpha():
                    r = trie_reverse.lookup_next(reversed_word[i])
                    if r == 1:
                        ans = reversed_word[last:i+1][::-1]
                        actual += str(num_map[ans])
                        break
                    elif  r == -1:
                        last = i
                    elif r == 0:
                        continue
                    elif r == -2:
                        last = i+1
                elif reversed_word[i].isdigit():
                    actual += reversed_word[i]
                    break
            
            
            self.__output+= actual+'\n'
            total_sum += int(actual)

        self.__output += str(total_sum)


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

